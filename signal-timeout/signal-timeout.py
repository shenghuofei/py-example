#-*- encoding:utf-8 -*-
import signal, os, time, threading

def handler(signum, frame):
    print 'Signal handler called with signal', signum, frame
    raise IOError("timeout!")

# Set the signal handler and a 5-second alarm
def do():
    signal.signal(signal.SIGALRM, handler) #must in main thread,listen SIGALRM signal
    signal.alarm(5)   #5s 后发送alarm信号,即超时时间
    try:
        time.sleep(8)
    except IOError:  #超时时间到了,handler跑出异常,捕获到异常后返回
        print "do timeout exit"
        signal.alarm(0)          # Disable the
        return 'exit'
    print "do done"    #未到超时时间继续后续逻辑
    signal.alarm(0)          # Disable the
    return 'do done'

def main():
    def th_handler(signum, frame):
        print 'Signal handler called with signal', signum, frame
        if thread.isAlive():
            print "thread timeout"
            thread._Thread__stop()
    
    def do_in_thread():
        for i in range(8):
            print "num %d" % i
            time.sleep(1)
        print "thread done"
        signal.alarm(0)          # Disable the
    
    signal.signal(signal.SIGALRM, th_handler) #must in main thread,listen SIGALRM signal
    signal.alarm(5)   #5s 后发送alarm信号,即超时时间

    thread = threading.Thread(target=do_in_thread)
    thread.start()
    time.sleep(5)   #主线程等待signal发送信号
    signal.alarm(0)          # Disable the
    return

do()
main()

#def alrm_handler(signum, frame):
#    raise AssertionError
#
#def sms_msgmail(action, cmd, retry=2):
#    errmsg = ''
#    signal.signal(signal.SIGALRM, alrm_handler)
#    # 等待子进程执行cmd命令，超时时间10s
#    signal.alarm(10)
#    s = subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=True)
#    try:
#        s.wait()
#        status = s.poll()
#        if status != 0:
#            for _ in range(retry):
#                s = subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=True)
#                s.wait()
#                status = s.poll()
#                if status == 0:
#                    errmsg = ''
#                    break
#                errmsg = 'Action: %s, status error: %s' % (action, s.stderr.read())
#    except AssertionError:
#        s.kill()
#        errmsg = 'Action: %s, error: cmd %s exec timeout' % (action, cmd)
#        return errmsg
#    except Exception, e:
#        errmsg = 'Action: %s, exception error: %s' % (action, str(e))
#    finally:
#        signal.alarm(0)
#    return errmsg

