<template>
	<div class="con">
		<div class="logo">
			<div class="logo">
				<img src="../img/logo.png" class="logo-img">
				<span class="logo-spa">统一身份认证</span>
			</div>
		</div>
		<div class="right">
			<div class="rightmain">
				<img class="icon" src="../img/Login/ewm.png">
				<section class="main">
					<div class="tabHead">
						<span style="width: 50%;" class="active">
							<a>账号登录</a>
						</span>
						<span style="width: 50%;">
							<a>动态码登录</a>
						</span>
					</div>
					<div class="login">
						<div>
							<div>
								<form action="" method="post">
									<div class="form">
				<!-- 用户名密码登录 -->  <div class="m-account">
											<div class="username item">
												<span class="prex-icon">
													<img src="../img/Login/user.png">
												</span> 
												<input id="username" name="username" type="text" placeholder="请输入学号/工号" title="请输入学号/工号">
											</div>
											<div class="password item">
												<span class="prex-icon">
													<img src="../img/Login/password.png">
												</span>
												<input id="password" name="passwordText" type="password" placeholder="请输入密码" title="请输入密码">
												<input id="saltPassword" name="password" type="hidden"><!-- <a class="input_eye suffix-icon eyehide"></a> -->
											</div>
											<div class="m-rememberMe">
												<input type="checkbox" name="rememberMe" id="rememberMe" value="true" style="width:15px;margin-right:5px;">
												<span>7天免登录</span>
											</div>
										</div>
										<div id="formErrorTip" class="form-errorTip">
											<span id="showErrorTip" class="form-error text-ellipsis"></span>
											<span id="showWarnTip" class="form-warn"></span>
										</div>
										<div class="botton" >
											<button id="login_submit" class="login-btn">登录</button>
										</div>
									</div>
								</form>
							</div>
						</div>

	<!-- 账户激活|忘记密码 -->
						<div class="help">
							<a id="retrievePassId" href="https://ca.csu.edu.cn/retrieve-password/retrievePassword/index.html#/?service=https%3A%2F%2Fmy.csu.edu.cn%2Fportal%2Findex.jsp" class="fo-password" title="通过手机短信、邮件方式找回密码">忘记密码</a>
							<div class="activation-account">
								<a id="activationAccountId" href="https://ca.csu.edu.cn/retrieve-password/accountActivation/index.html#/?service=https%3A%2F%2Fmy.csu.edu.cn%2Fportal%2Findex.jsp" class="activation-account">账号激活</a>
							</div>
						</div>
						<div class="help">
							<a id="zhsshu" target="_blank" style="text-decoration: none;font-size: 14px;color: #73757E;" href="https://ca.csu.edu.cn/emap/sys/zndxzhss/*default/indexsq.do" title="无法通过手机短信、邮件方式找回密码">账号申诉</a>
							<a id="zhsqing" target="_blank" style="position: absolute;right: 0;text-decoration: none;font-size: 14px;color: #0c4af9;" href="https://ca.csu.edu.cn/emap/sys/zndxzhsq/*default/indexsq.do">账号申请</a>
						</div>
				</div>
			</section>
			<div class="footer">
				<div  style="color: #0c4af9;min-width: 100px;float: left;margin-right: 10px;">其他登录方式</div>
				<div class="login-icon">
					<div class="item">
						<a id="combinedLogin_a_qq" href="https://ca.csu.edu.cn/authserver/combinedLogin.do?type=qq&amp;success=https%3A%2F%2Fmy.csu.edu.cn%2Fportal%2Findex.jsp">
							<img src="../img/Login/qq.png" >
						</a>
					</div>
					</div>
						<div class="login-icon">
							<div class="item">
								<a id="combinedLogin_a_weiXin" href="https://ca.csu.edu.cn/authserver/combinedLogin.do?type=weixin&amp;success=https%3A%2F%2Fmy.csu.edu.cn%2Fportal%2Findex.jsp">
									<img src="../img/Login/weixin.png" >
								</a>
							</div>
						</div>
					</div>
				</div>
			<p class="wenzi">版权所有 © 2020 中南大学信息与网络中心. 保留所有权利技术支持：0731-88830426  邮箱地址：app@csu.edu.cn</p>
			<div class="lang_switch t_switch">
				<select id="language" class="switch_list">
	       			<option value="zh_CN" selected="selected">简体中文</option>
					<option value="en">English</option>
				</select>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'login',
		data() {
			return {
				msg: "登录"
			}
		}
	}
</script>

<style>
.con{
	background-image: url(../img/Login/bg.png);
	position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
.logo{
    position: absolute;
    top: 50px;
    left: 10%;
}
.logo-img {
    width: 246px;
}
.logo-spa{
    display: inline-block;
    position: absolute;
    height: 38px;
    line-height: 38px;
    top: 15px;
    margin-left: 15px;
    padding-left: 15px;
    border-left: 1px solid #fff;
    color: #fff;
    font-size: 24px;
    width: 150px;
}
.right{
    width: 600px;
    height: 100vh;
    background: rgba(0,0,0,0.3);
    position: absolute;
    top: 0;
    right: 0;
}
.rightmain{
    width: 416px;
    max-height: 531px;
    min-height: 456px;
    position: relative;
    background: #ffffff;
    border-radius: 4px;
    margin: 20% auto 0;
}
.icon{
    width: 60px;
    height: 60px;
    position: absolute;
    top: 0;
    right: 0;
    cursor: pointer;
}
.main {
    width: calc(100% - 76px);
    min-height: 300px;
    padding: 22px 38px;
}
.tabHead {
    width: 100%;
    z-index: 10;
    overflow: hidden;
    font-size: 12px;
    border-bottom: 1px solid #DEDEDE;
}
.tabHead span {
    display: block;
    width: 80px;
    float: left;
    position: relative;
    z-index: 2;
    font-size: 18px;
    text-align: center;
    cursor: pointer;
    line-height: 20px;
    padding: 8px 0;
}
.login {
    position: relative;
}
.form {
    display: block;
    margin-top: 0em;
    margin-block-end: 1em;
}
.form {
    margin-top: 10px;
}
.m-account{
    border-radius: 5px;
    background: #fff;
}
.form .m-account .item{
    border-width: 1px;
    border-style: solid;
    border-color: #e8e8e8;
    border-radius: 4px;
    height: 48px;
    margin-top: 20px;
}
.prex-icon{
    position: absolute;
    top: 4px;
    left: 2px;
}
.uop_icon{

}
.m-account > div{
    position: relative;
    overflow: hidden;
}
.form .m-account > div > input{
    width: 70%;
    border: none;
    height: 48px;
    margin-left: 48px;
    outline: none;
}
#rememberMe {
    margin-left: 0;
    height: auto;
	margin-top: 10px;
}
.btn {
    margin-top: 30px;
}
.botton {
    margin-top: 30px;
}
.login-btn {
    width: 100%;
    height: 50px;
    background: #2368de;
    border-radius: 4px;
    display: block;
    color: #fff;
    text-align: center;
    line-height: 50px;
    font-size: 18px;
    text-decoration: none;
    letter-spacing: 12px;
}
.help {
    position: relative;
    clear: both;
    margin-top: 12px;
    height: 26px;
}
.fo-password {
    text-decoration: none;
    font-size: 14px;
    line-height: 26px;
    color: #73757E;
    float: left;
}
.activation-account {
    text-decoration: none;
    font-size: 14px;
    line-height: 26px;
    color: #0c4af9;
    float: right;
}
.footer {
    width: calc(100% - 64px);
    position: absolute;
    bottom: 0px;
    left: 0px;
    height: 58px;
    background: #F3F8FE;
    border-radius: 0 0 6px 6px;
    display: flex;
    align-items: Center;
    padding: 0 32px;
}
.login-icon{
    width: 60px;
    float: left;
}
.login-icon img{
	width: 32px;
}
.wenzi{
    width: 416px;
    margin: 20px auto 0;
    font-size: 12px;
    color: #FFFFFF;
    line-height: 24px;
}
.lang_switch {
    width: 104px;
    top: 50px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    background: rgba(12,74,249,0.30);
}
.t_switch {
    height: 28px;
    position: absolute;
    text-align: left;
    cursor: pointer;
    right: 10%;
    border-radius: 4px;
    font-size: 14px;
}
.switch_list {
    padding: 5px 14px;
    background: #ffffff;
    box-shadow: 0 6px 6px -2px rgb(40 75 96 / 18%);
    border-radius: 4px;
}
.active {
    border-bottom: 1px solid #2B6CDB;
}
.tabHead span.active a {
    color: #2B6CDB;
}
</style>

