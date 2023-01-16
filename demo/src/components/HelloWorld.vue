<template>
  <div class="all">
    <div style="display: flex;z-index: 999;;width: 100%;height: 60px;background-color: dodgerblue;align-items: row;justify-content: center; position: fixed;">
      <div id="head" style="width:1030px">
        <div>
          <img src="../img/logo.png">
        </div>
        <div>
        信息门户
        </div>
      </div>
    </div>
    <div class="ban"></div>
    <div style="display:flex;justify-content:center;width: 100%;">
      <div id="main-body">
        <!--左侧-->
        <div class="mleft">
          <!--用户栏-->
          <div class="border-user">
            <div class="user">
              <div class="user-pic">
                <img >
              </div>
              <p class="user-name">王玉玺</p>
              <div class="address-select">
                <label>
                  <span id="statusValue" style="margin-left:30px;cursor: pointer;">
                    空闲
                  </span>
                  <i class="address-arrow-down"></i>
                </label>
              </div>
              <p class="user-handle">
                <a class="module_link" target="_blank">个人信息</a>
                <span>|</span>
                <a class="module_link">退出登录</a>
              </p>
            </div>
          </div>
          <!--单点登录-->
          <div class="border">
            <div class="sign-login" id="ajaxSso">
              <div class="login-title js_more_sso">
                <img src="../img/login_title.png">
                <img src="../img/set_ico.png" class="set-ico" id="moreSso">
              </div>
              <ul class="login-link" id="ssoList" style="min-height: 335px;">
		            <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="新生自助服务" systemid="16" channelname="xszzfw" ssourl="http://Newcomer.its.csu.edu.cn/sso.aspx">
			            <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/30.png" width="44px" height="44px">
			            <p style="text-align: center;width: 100%">新生自助..</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="本科生教务" systemid="52" channelname="xcsubkjw" ssourl="http://csujwc.its.csu.edu.cn/sso.jsp">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/17.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">本科生教务</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="中南云盘" systemid="70" channelname="aishuwpang" ssourl="http://pan.csu.edu.cn/sso">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/70.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">中南云盘</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="公文协同" systemid="13" channelname="csugzpt" ssourl="http://oa.csu.edu.cn">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/13.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">公文协同</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="档案系统" systemid="19" channelname="tsglpt" ssourl="http://202.197.71.187:8060/DAS/login.jsp">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/19.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">档案系统</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="离校系统" systemid="20" channelname="lxxt" ssourl="http://lxxt.its.csu.edu.cn/sso.aspx">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/31.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">离校系统</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="新闻网投稿系统" systemid="22" channelname="xwtgxt" ssourl="https://zzgl.csu.edu.cn/system/contribute/caslogin.jsp">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/32.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">新闻网投..</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="竞价网" systemid="27" channelname="jjwxt" ssourl="http://202.197.61.27:8088/bid">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/34.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">竞价网</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="档案服务系统" systemid="28" channelname="csudaywxt" ssourl="http://202.197.71.187:8060/ZNZG/login.jsp">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/35.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">档案服务..</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="易班" systemid="35" channelname="csuybxtpt" ssourl="http://yiban.csu.edu.cn/yjdl/yb_login">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/36.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">易班</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="财务平台" systemid="44" channelname="cwcjsb" ssourl="http://cwpt.csu.edu.cn/caslogin.aspx">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/39.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">财务平台</p> 
                </li>
                <li class="js_ssoitem" style="padding: 5px; cursor: pointer; background-color: rgb(255, 255, 255);" title="虚拟仿真实验平台1" systemid="46" channelname="xyfzsypt" ssourl="http://122.207.105.30:6553/yqfz/reg/Connect.php">
                  <img src="https://app.its.csu.edu.cn/fe/systemimg/ssosystem/41.png" width="44px" height="44px">
                  <p style="text-align: center;width: 100%">虚拟仿真..</p> 
                </li>
              </ul>
            </div>
          </div>
          <!--中大信息-->
          <div class="border">
            <div class="school-inform">
              <a target="_blank" href="http://oa.csu.edu.cn/con/hdjb">
                <div class="inform-title">
                  <img src="../img/school-inform.png">
                  <img id="more" src="../img/more-ico.png" style=" position: absolute; right: 20px; top: 11px; margin-right: -6px; cursor: pointer;">
                </div>
              </a>
            </div>
          </div>
          <!--校内通知-->
          <div class="border">
            <div class="school-inform" id="latest">
		          <a target="_blank" href="http://oa.csu.edu.cn/con/ggtz">
                <div class="inform-title">
			            <img src="../img/anounce.png">
                  <img id="more" src="../img/more-ico.png" style=" position: absolute; right: 20px; top: 11px; margin-right: -6px; cursor: pointer;">		            </div>
              </a>
            </div>
          </div>
        </div>
        <!--中间-->
        <div class="mmiddle">
        </div>
        <!--右边-->
        <div class="mright">
          <!--日历-->
          <div class="border">
            <div class="inform-title" style="padding-bottom: 0px;margin-bottom: 0px">
              <a target="_blank" href="https://my.csu.edu.cn/portal/schedule.jsp">
                <img src="../img/my_schedule.png">
                <i style="display: block; width: 40px; height: 16px; background: url(&quot;../portal/images/more.png&quot;); position: absolute; right: 20px; top: 11px; margin-right: -6px; cursor: pointer;" id="moreApps">
                </i>
              </a>
            </div>
            <div id="zabuto_calendar_x9y" style="margin-top: 1px;">
              <div class="zabuto_calendar" id="zabuto_calendar_x9y">
                <table class="table">
                  <tbody>
                    <tr class="calendar-month-header">
                      <th>
                        <div class="calendar-month-navigation" id="zabuto_calendar_x9y_nav-prev">
                          <span>
                            <div class="last-month" style="margin-top:0px;font-size:3px;font-family:微软雅黑;">
                              &nbsp;
                            </div>
                          </span>
                        </div>
                      </th>
                      <th colspan="5">
                        <span>
                          1月
                        </span>
                      </th>
                      <th>
                        <div class="calendar-month-navigation" id="zabuto_calendar_x9y_nav-next">
                          <span>
                            <div class="next-month" style="margin-top:0px;font-size:3px;font-family:微软雅黑;">
                              &nbsp;
                            </div>
                          </span>
                        </div>
                      </th>
                    </tr>
                    <tr class="calendar-dow-header">
                      <th>SUN</th>
                      <th>MON</th>
                      <th>TUE</th>
                      <th>WED</th>
                      <th>THU</th>
                      <th>FRI</th>
                      <th>SAT</th>
                    </tr>
                    <tr class="calendar-dow">
                      <td id="zabuto_calendar_x9y_2023-01-01" class="dow-clickable">
                        <div id="zabuto_calendar_x9y_2023-01-01_day" class="day">
                          <span class="commonday">1</span>
                          <span class="lunarday">初十</span>
                        </div>
                      </td>
                      <td id="zabuto_calendar_x9y_2023-01-02" class="dow-clickable">
                        <div id="zabuto_calendar_x9y_2023-01-02_day" class="day">
                          <span class="commonday">2</span>
                          <span class="lunarday">十一</span>
                        </div>
                      </td>
                      <td id="zabuto_calendar_x9y_2023-01-03" class="dow-clickable">
                        <div id="zabuto_calendar_x9y_2023-01-03_day" class="day">
                          <span class="commonday">3</span>
                          <span class="lunarday">十二</span>
                        </div>
                      </td>
                      <td id="zabuto_calendar_x9y_2023-01-04" class="dow-clickable">
                        <div id="zabuto_calendar_x9y_2023-01-04_day" class="day">
                          <span class="commonday">4</span>
                          <span class="lunarday">十三</span>
                        </div>
                      </td>
                      <td id="zabuto_calendar_x9y_2023-01-05" class="dow-clickable">
                        <div id="zabuto_calendar_x9y_2023-01-05_day" class="day">
                          <span class="commonday">5</span>
                          <span class="lunarday">十四</span>
                        </div>
                      </td>
                      <td id="zabuto_calendar_x9y_2023-01-06" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-06_day" class="day"><span class="commonday">6</span><span class="lunarday">十五</span></div></td><td id="zabuto_calendar_x9y_2023-01-07" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-07_day" class="day"><span class="commonday">7</span><span class="lunarday">十六</span></div></td></tr><tr class="calendar-dow"><td id="zabuto_calendar_x9y_2023-01-08" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-08_day" class="day"><span class="commonday">8</span><span class="lunarday">十七</span></div></td><td id="zabuto_calendar_x9y_2023-01-09" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-09_day" class="day"><span class="commonday">9</span><span class="lunarday">十八</span></div></td><td id="zabuto_calendar_x9y_2023-01-10" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-10_day" class="day"><span class="commonday">10</span><span class="lunarday">十九</span></div></td><td id="zabuto_calendar_x9y_2023-01-11" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-11_day" class="todaydiv"><span class="todaycommonday">11</span><span class="todaylunarday">二十</span></div></td><td id="zabuto_calendar_x9y_2023-01-12" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-12_day" class="day"><span class="commonday">12</span><span class="lunarday">廿一</span></div></td><td id="zabuto_calendar_x9y_2023-01-13" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-13_day" class="day"><span class="commonday">13</span><span class="lunarday">廿二</span></div></td><td id="zabuto_calendar_x9y_2023-01-14" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-14_day" class="day"><span class="commonday">14</span><span class="lunarday">廿三</span></div></td></tr><tr class="calendar-dow"><td id="zabuto_calendar_x9y_2023-01-15" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-15_day" class="day"><span class="commonday">15</span><span class="lunarday">廿四</span></div></td><td id="zabuto_calendar_x9y_2023-01-16" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-16_day" class="day"><span class="commonday">16</span><span class="lunarday">廿五</span></div></td><td id="zabuto_calendar_x9y_2023-01-17" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-17_day" class="day"><span class="commonday">17</span><span class="lunarday">廿六</span></div></td><td id="zabuto_calendar_x9y_2023-01-18" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-18_day" class="day"><span class="commonday">18</span><span class="lunarday">廿七</span></div></td><td id="zabuto_calendar_x9y_2023-01-19" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-19_day" class="day"><span class="commonday">19</span><span class="lunarday">廿八</span></div></td><td id="zabuto_calendar_x9y_2023-01-20" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-20_day" class="day"><span class="commonday">20</span><span class="lunarday">廿九</span></div></td><td id="zabuto_calendar_x9y_2023-01-21" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-21_day" class="day"><span class="commonday">21</span><span class="lunarday">三十</span></div></td></tr><tr class="calendar-dow"><td id="zabuto_calendar_x9y_2023-01-22" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-22_day" class="day"><span class="commonday">22</span><span class="lunarday">正月</span></div></td><td id="zabuto_calendar_x9y_2023-01-23" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-23_day" class="day"><span class="commonday">23</span><span class="lunarday">初二</span></div></td><td id="zabuto_calendar_x9y_2023-01-24" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-24_day" class="day"><span class="commonday">24</span><span class="lunarday">初三</span></div></td><td id="zabuto_calendar_x9y_2023-01-25" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-25_day" class="day"><span class="commonday">25</span><span class="lunarday">初四</span></div></td><td id="zabuto_calendar_x9y_2023-01-26" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-26_day" class="day"><span class="commonday">26</span><span class="lunarday">初五</span></div></td><td id="zabuto_calendar_x9y_2023-01-27" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-27_day" class="day"><span class="commonday">27</span><span class="lunarday">初六</span></div></td><td id="zabuto_calendar_x9y_2023-01-28" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-28_day" class="day"><span class="commonday">28</span><span class="lunarday">初七</span></div></td></tr><tr class="calendar-dow"><td id="zabuto_calendar_x9y_2023-01-29" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-29_day" class="day"><span class="commonday">29</span><span class="lunarday">初八</span></div></td><td id="zabuto_calendar_x9y_2023-01-30" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-30_day" class="day"><span class="commonday">30</span><span class="lunarday">初九</span></div></td><td id="zabuto_calendar_x9y_2023-01-31" class="dow-clickable"><div id="zabuto_calendar_x9y_2023-01-31_day" class="day"><span class="commonday">31</span><span class="lunarday">初十</span></div></td><td></td><td></td><td></td><td></td>
                    </tr>
                  </tbody>
                </table>
                <div class="legend" id="zabuto_calendar_x9y_legend">
                </div>
              </div>
            </div>
          </div>
          <!--我的应用-->
          <div class="border">
            <div class="sign-login" id="ajaxApps">
              <div id="appTitle" class="login-title js_more_apps" >
                <img src="../img/store_title.png">
                <img class="more-ico" id="moreApps" src="../img/more-ico.png">
              </div>
              <ul id="indexAppList" class="login-link">
              <li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="报到注册" appid="PUB_2017083011421111060">
                <img src="http://app.its.csu.edu.cn/fe/upload/appserver/2017/09/05/20170905224806867731.jpg" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">报到注册</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="自习教室" appid="PUB_2014122416494110840">
                <img src="http://app.its.csu.edu.cn/fe/upload/2014/12/24/20141224165755256536.jpg" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">自习教室</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="校内通知" appid="PUB_6">
                <img src="http://app.its.csu.edu.cn/fe/upload/2014/11/24/20141124094440391895.jpg" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">校内通知</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="学校要闻" appid="PUB_5">
                <img src="http://app.its.csu.edu.cn/fe/upload/2014/09/18/20140918200028732240.png" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">学校要闻</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="校园卡服务" appid="PUB_1417104050376873">
                <img src="http://app.its.csu.edu.cn/fe/upload/appserver/2017/02/20/20170220152224528042.jpg" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">校园卡服务</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="本科生课表" appid="PUB_1">
                <img src="http://app.its.csu.edu.cn/fe/upload/2014/09/18/20140918163918462706.png" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">本科生课表</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="班车服务" appid="PUB_3">
                <img src="http://app.its.csu.edu.cn/fe/upload/2014/09/18/20140918163949839445.png" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">班车服务</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="中南黄页" appid="PUB_2">
                <img src="http://app.its.csu.edu.cn/fe/upload/2014/09/18/20140918164012816525.png" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">中南黄页</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li><li id="indexApp" class="js_ssoitem" style="padding: 5px; cursor: pointer; position: relative; background-color: rgb(255, 255, 255);" title="易家" appid="PUB_1425036327847772">
                <img src="http://app.its.csu.edu.cn/fe/upload/2015/02/27/20150227113202416879.jpg" width="44px" height="44px" class="avatar">
                <p style="text-align: center;width: 100%">易家</p>
                <p id="indexMsgCount" class="appxxim_msgCount" style="display: none; position: absolute; right: 0px; top: -5px; color: rgb(255, 255, 255);">1</p>
              </li></ul>
            </div>
          </div>
          <!--资金-->
          <div class="border">
            <div id="money">
              <div id="money-title">
                <img src="../img/money_title.png">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-box" >
		  <div class="footer">
			  <div style="width: 100%;text-align: center">中南大学版权所有&nbsp;&nbsp;湘ICP备05005659&nbsp;&nbsp;技术支持：0731-88877894&nbsp;&nbsp;邮箱地址：app@csu.edu.cn</div>
		  </div>
	  </div>
  </div>
</template>

<script>
</script>

<style>
.all{
  background-color: #ededed;
  display: flex;
  flex-flow: column;
}
  #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#head {
  display: flex;
  flex-direction: row;
  position: fixed;
  align-items: center;
  height: 60px;
  width: 100%;
  background-color: dodgerblue;
  font-size:x-large;
  color: white;
  border-right: 10px;
  z-index: 9999;
}
.ban{
  height: 60px;
  position: relative;
}
#main-body{
  display: flex;
  height: 100%;
  width: 1030px;
  align-items: row;
  background-image: url(../img/banner.png);
  background-repeat:no-repeat;
}
.mleft{
  float: left;
  width: 230px;
  margin-top: 105px;
}
.mmiddle{
  float: left;
  width: 540px;
  margin-left: 15px;
  margin-top: 15px;
}
.mright{
  float: right;
  width: 230px;
  margin-top: 150px;
}
.border-user {
  background-color: #fff;
  opacity: 30% false;
    border-left: 1px solid #dbdadb;
    border-right: 1px solid #dbdadb;
    border-bottom: 1px solid #dbdadb;
    margin-bottom: 10px;
}
.user{
  border-bottom: 1px solid #b8b6b7;
  padding: 5px 0 15px 0;
}
.user-pic{
  width: 82px;
  height: 82px;
  margin: auto;
  cursor: pointer;
}
.user-name {
    text-align: center;
    color: #3E3E3E;
    font-size: 14px;
    margin-top: 20px;
}
.address-select {
    position: relative;
    width: 130px;
    margin: 10px auto 0 auto;
}
.address-arrow-down {
    display: block;
    width: 9px;
    height: 7px;
    position: absolute;
    right: 10px;
    top: 12px;
}
.user-handle {
    font-size: 12px;
    text-align: center;
    color: #3E3E3E;
    margin-top: 10px;
}
.module_link {
    color: #3e3e3e;
    font-size: 12px;
}
.border {
    border-left: 1px solid #dbdadb;
    border-right: 1px solid #dbdadb;
    border-bottom: 1px solid #dbdadb;
    background-color: #ffffff;
    margin-bottom: 10px;
}
.sign-login {
    border-bottom: 1px solid #b8b6b7;
    padding: 5px 0 15px 0;
}
.login-title {
    margin-left: 10px;
    padding-bottom: 0px;
    position: relative;
}
.set-ico {
    display: block;
    width: 17px;
    height: 17px;
    position: absolute;
    right: 30px;
    top: 11px;
    margin-right: -6px;
    cursor: pointer;
}
.login-link {
    overflow: hidden;
    margin: 0 8px 0 8px;
    padding: 0;
}
.login-link p {
    font-size: 12px;
    color: #747474;
    text-align: center;
    display: inline-block;
}
.login-link li {
    float: left;
    margin-top: 10px;
    width: 60px;
    padding-left: 4px;
    padding-right: 4px;
    list-style:none
}
.school-inform {
    border-bottom: 1px solid #b8b6b7;
    padding: 5px 0 15px 0;
}
.inform-title {
    margin-left: 10px;
    padding-bottom: 0px;
    position: relative;
}
.zabuto_calendar {
    margin: 0;
    padding: 0;
    text-align: center;
}
.table {
    width: 96%;
    padding: 0;
    margin: auto;
    font-size: 14px;
    background-color: #fff;
    text-align: center;
    border-top: 1px solid #e7e7eb;
    border-bottom: 1px solid #e7e7eb;
}
.calendar-dow-header th {
    border-top: 1px solid #ccc8c8;
    font-size: 12px;
    color: #BCBCBC;
    font-weight: normal;
    width: 16px;
    line-height: 18px;
}
.zabuto_calendar tr td:first-child {
    color: #4393c1;
}
.zabuto_calendar tr td:last-child {
    color: #4393c1;
}
.day {
    margin: 0;
    padding-top: 7px;
    padding-bottom: 7px;
    width: auto;
}
.commonday {
    display: block;
    line-height: 12px;
    font-size: 10px;
}
.lunarday {
    display: block;
    line-height: 12px;
    font-size: 10px;
}
.last-month {
    margin-top: 5px;
    background: url(../img/tleft.png) no-repeat right center;
    line-height: 12px;
    width: 23px;
    text-align: left;
}
.next-month {
    margin-top: 5px;
    background: url(../img/tright.png) no-repeat right center;
    line-height: 12px;
    width: 23px;
    text-align: left;
}
.more-ico{
  display: block;
    width: 40px;
    height: 16px;
}
.footer-box {
    width: 100%;
    background-color: #0082fe;
    height: 40px;
}
.footer {
    width: 1030px;
    margin: auto;
    color: #FFFFFF;
    font-size: 12px;
    line-height: 40px;
}
</style>