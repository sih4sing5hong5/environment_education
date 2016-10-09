import React from 'react';
import Promise from 'bluebird';
var superagent = require('superagent-promise')(require('superagent'), Promise);
import './電視.css';
import 後端 from '../App/後端';

import Debug from 'debug';
var debug = Debug('env:電視');

export default class 電視 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      全部題目: [
        // { '題號': '10', '題目': '500', '選項1': 510, '選項2': 5102, '選項3': 5103, '選項4': 5104, '答案': 1, '解析': '解析' },
        // { '題號': '20', '題目': '500', '選項1': 510, '選項2': 5102, '選項3': 510, '選項4': 5104, '答案': 3, '解析': '解析' },
        // { '題號': '30', '題目': '500', '選項1': 510, '選項2': 510, '選項3': 5103, '選項4': 5104, '答案': 2, '解析': '解析' },
        // { '題號': '40', '題目': '500', '選項1': 510, '選項2': 5102, '選項3': 5103, '選項4': 510, '答案': 4, '解析': '解析' },
      ],
      狀態: '猶未開始',
    };
    this.掠();
  }

  componentWillMount() {
    this.減秒timer = setInterval(this.減秒.bind(this), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.減秒timer);
  }

  掠() {
    superagent.get(後端.網址() + '搶答題目')
        .withCredentials()
      .then(({ body }) => (this.setState(body)))
      .catch((err) => (debug(err)));
  }

  開始() {
    this.setState({ 狀態: '比賽', 這馬第幾題: 0, 春幾秒: 15, });
  }

  減秒() {
    let { 狀態 } = this.state;
    let 新秒 = this.state.春幾秒 - 1;
    this.setState({ 春幾秒: 新秒 });
    if (新秒 <= 0 && 狀態 == '比賽')
      this.毋著();
  }

  選(選項) {
    let { 全部題目, 這馬第幾題 } = this.state;
    let 題目 = 全部題目[這馬第幾題];
    if (題目.答案 == 選項)
    {
      let 這馬第幾題 = this.state.這馬第幾題 + 1;
      this.setState({
        這馬第幾題: 這馬第幾題,
        春幾秒: 10,
      });

      if (這馬第幾題 >= 全部題目.length)    {
        this.setState({ 狀態: '攏著' });
        let 全部題號 = 全部題目.filter((題目, i)=>(i <= 這馬第幾題)).map((題目)=>(題目.題號));
        let 內容 = {
          答對: JSON.stringify(全部題號),
          答錯: JSON.stringify([]),
        };
        superagent.post(後端.網址() + '送出搶答')
          .withCredentials()
          .set('Content-Type', 'application/x-www-form-urlencoded')
          .send(內容)
          .then(({ body })=>(1))
          .catch((err)=>debug(err));
      }
    } else
      this.毋著();
  }

  毋著() {
    this.setState({ 狀態: '毋著' });
    let { 全部題目, 這馬第幾題 } = this.state;
    let 全部題號 = 全部題目.filter((題目, i)=>(i < 這馬第幾題)).map((題目)=>(題目.題號));
    let 內容 = {
      答對: JSON.stringify(全部題號),
      答錯: JSON.stringify([全部題目[這馬第幾題].題號]),
    };
    superagent.post(後端.網址() + '送出搶答')
      .withCredentials()
      .set('Content-Type', 'application/x-www-form-urlencoded')
      .send(內容)
      .then(({ body })=>(1))
      .catch((err)=>debug(err));
  }

  render() {
    let { 狀態, 全部題目, 這馬第幾題, 春幾秒 } = this.state;
    if (狀態 == '猶未開始' && 全部題目.length == 0)    {
      return (
        <div>
          <h1 className="ui dividing header">環保知識挑戰擂台賽</h1>    
          題目載入中
        </div>
        );
    }

    if (狀態 == '猶未開始')    {
      return (
        <div>
          <h1 className="ui dividing header">環保知識挑戰擂台賽</h1>    
        <button className='ui massive button green' onClick={this.開始.bind(this)}>開始</button>
        </div>
        );
    }

    if (狀態 == '毋著')    {
      let 毋著題 = 全部題目[這馬第幾題];
      return (
      <div id='電視'>
          <h1 className="ui dividing header">第{這馬第幾題 + 1}題答錯了</h1>   
          <h2 className="ui  header">{毋著題.題目}</h2>    
        <ul>
         <li>{毋著題.選項1}</li>
         <li>{毋著題.選項2}</li>
         <li>{毋著題.選項3}</li>
         <li>{毋著題.選項4}</li>
        </ul>
          <h2 className="ui  header">{毋著題.解析}</h2>    
          <h3 className="ui  header">答案:{毋著題.答案}</h3>    
        </div>
        );
    }

    if (狀態 == '攏著')    {
      let 全部題號 = 全部題目.filter((題目, i)=>(i <= 這馬第幾題)).map((題目)=>(題目.題號));
      return (
        <div>
          <h1 className="ui dividing header">{全部題號.length}題都答對 !!!!</h1>    
        </div>
        );
    }

    let 題目 = 全部題目[這馬第幾題];
    return (
      <div id='電視'>
        <h1 className="ui dividing header">{這馬第幾題+1}. {題目.題目}</h1>  
        <ul>
         <li>{題目.選項1}</li>
         <li>{題目.選項2}</li>
         <li>{題目.選項3}</li>
         <li>{題目.選項4}</li>
        </ul>
        <button className='ui massive button green' onClick={this.選.bind(this, 1)}>1</button>
        <button className='ui massive button green' onClick={this.選.bind(this, 2)}>2</button>
        <button className='ui massive button green' onClick={this.選.bind(this, 3)}>3</button>
        <button className='ui massive button green' onClick={this.選.bind(this, 4)}>4</button>
        <span>{春幾秒}</span>
      </div>
    );
  }
}
