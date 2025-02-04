git pull origin main#从云端下载代码


1. **确保您已克隆仓库**：
   如果尚未克隆仓库，请使用以下命令（但请注意，由于 GitHub 已不再支持密码认证，您可能需要使用 SSH URL 或配置 Git 凭据以使用个人访问令牌）：
   ```bash
   git clone https://github.com/34zkx/try1.git
   cd try1
   ```
  

2. **将文件添加到仓库**：
   将您想要发送的文件复制到仓库的目录中（如果文件不在那里的话）。然后，使用 `git add` 命令将文件添加到暂存区：
   ```bash
   git add your-file-name
   git add . #添加全部
   ```
   替换 `your-file-name` 为实际的文件名。

3. **提交更改**：
   使用 `git commit` 命令提交您的更改：
   ```bash
   git commit -m "Add your file description"
   ```
   替换 `"Add your file description"` 为实际的提交信息。

4. **推送到远程仓库**：
   最后，使用 `git push` 命令将您的更改推送到远程仓库：
   ```bash
   git push origin main
   ```
   或者，如果您的默认分支不是 `main`（例如是 `master`），请将 `main` 替换为实际的分支名。

   如果您在推送时遇到认证问题，并且您正在使用 SSH URL，请确保您的 SSH 密钥已正确配置，并且您已经将其公钥添加到了 GitHub 帐户中。如果您使用的是 HTTPS URL，并且没有配置 Git 凭据助手或使用个人访问令牌，则可能需要手动输入您的 GitHub 用户名和令牌（但请注意，直接在命令行中输入令牌是不安全的，建议使用 Git 凭据助手来安全地存储凭据）。
##API 代替密码进行提交
    

请遵循这些步骤，您应该能够成功地将文件发送到 GitHub 上的仓库。如果您在过程中遇到任何问题，请确保检查您的 Git 配置、网络连接以及 GitHub 帐户的权限设置。