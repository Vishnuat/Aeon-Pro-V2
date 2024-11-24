from bot import CMD_SUFFIX as i


class _BotCommands:
    def __init__(self):
        self.StartCommand = "start"
        self.MirrorCommand = [f"mirror{i}", f"m{i}"]
        self.YtdlCommand = [f"ytdl{i}", f"y{i}"]
        self.LeechCommand = [f"leech{i}", f"l{i}"]
        self.YtdlLeechCommand = [f"ytdlleech{i}", f"yl{i}"]
        self.CloneCommand = [f"clone{i}", f"c{i}"]
        self.CountCommand = f"count{i}"
        self.DeleteCommand = f"del{i}"
        self.StopAllCommand = [f"stopall{i}", "stopallbot"]
        self.ListCommand = f"list{i}"
        self.SearchCommand = f"search{i}"
        self.StatusCommand = [f"status{i}", f"s{i}", "statusall"]
        self.UsersCommand = f"users{i}"
        self.AuthorizeCommand = [f"authorize{i}", f"a{i}"]
        self.UnAuthorizeCommand = [f"unauthorize{i}", f"ua{i}"]
        self.AddSudoCommand = f"addsudo{i}"
        self.RmSudoCommand = f"rmsudo{i}"
        self.PingCommand = ["ping", "p"]
        self.RestartCommand = [f"restart{i}", f"r{i}", "restartall"]
        self.StatsCommand = [f"stats{i}", "statsall"]
        self.HelpCommand = [f"help{i}", f"h{i}"]
        self.LogCommand = f"log{i}"
        self.ShellCommand = f"shell{i}"
        self.EvalCommand = f"eval{i}"
        self.ExecCommand = f"exec{i}"
        self.BotSetCommand = [f"botsettings{i}", f"bs{i}"]
        self.UserSetCommand = [f"usetting{i}", f"us{i}"]
        self.SpeedCommand = [f"speedtest{i}", f"sp{i}"]
        self.AddImageCommand = f"addimg{i}"
        self.ImagesCommand = f"images{i}"
        self.MediaInfoCommand = [f"mediainfo{i}", f"mi{i}"]
        self.BroadcastCommand = [f"broadcast{i}", "broadcastall"]


BotCommands = _BotCommands()
