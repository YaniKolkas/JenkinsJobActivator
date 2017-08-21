import jenkins_handler as jh
import main_window as mw


def main():

    def_job_url = "http://localhost:8080/job/remote_activation/"
    def_token = "SOMAMU"
    entry_url_mw, token_mw, job_param_mw, text_output_mw, button_mw =\
        mw.create_gui(def_job_url, def_token)

    button_mw.config(command=lambda: job_call(entry_url_mw, token_mw, job_param_mw, text_output_mw) )

    mw.star_gui()


def job_call(url_gui_el, token_gui_el, job_param_gui_el, text_output_mw):

    url = url_gui_el.get()
    token = token_gui_el.get()
    job_param =job_param_gui_el.get()


    print "JOB CALLED WITH FOLLOWING PARAMS"
    print "URL = {}".format(url)
    print "TOKEN = {}".format(token)
    print "JOB PARAM = {}".format(job_param)

    params = {'token': token,
              'JIRA_STORY' : job_param }

    jh.activate_job(url,params )

    txt = 'JOB ACTIVATED:\n' \
          'URL = {}\n' \
          'TOKEN = {}\n' \
          'JOB PARAM = {}\n'.format(url,token,job_param)

    text_output_mw.insert(mw.index_insert, txt)

if __name__ == "__main__":
    main()