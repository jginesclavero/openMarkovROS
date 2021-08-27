#!/usr/bin/env python

import rospy
from py4j.java_gateway import JavaGateway, GatewayParameters
from openmarkov_roswrap.srv import SetFinding, SetFindingResponse, GetVarProbs, GetVarProbsResponse
from openmarkov_roswrap.msg import OMvariable, StateWithProb

class OpenMarkovROS:
  def __init__(self):
    rospy.Service('/openmarkov_ros/set_finding', SetFinding, self.setFindingCB)
    rospy.Service('/openmarkov_ros/get_var_probs', GetVarProbs, self.getVarProbsCB)

    self.gateway_ = JavaGateway(gateway_parameters = GatewayParameters(auto_convert = True))
    self.gateway_.entry_point.initNet(
      "ActivityRecognition_Experiment1NACO.pgmx",
      "/home/jgines/Documents/Congresos_y_publicaciones/publications_urjculelux/2019/Journal/NACO/OpenMarkovExperiments/"
    )
    self.probNet_ = self.gateway_.entry_point.getProbNet()
    # print (self.probNet_)

  def setFindingCB(self, data):
    probs = self.gateway_.entry_point.setFinding(data.variable, data.state)
    # for var in probs:
    #   if str(var) == data.variable:
    #     print (data.variable)
    #     values = probs[var].getValues()
    #     cont = 0
    #     for i in values:
    #       state = StateWithProb()
    #       state.state = var.getStateName(cont)
    #       state.prob = i
    #       print (state)
    #       cont += 1
    return SetFindingResponse()

  def getVarProbsCB(self, data):
    evidence = self.gateway_.entry_point.getEvidence()
    probs = self.gateway_.entry_point.getPropagation(evidence)
    variable_msg = OMvariable()
    for var in probs:
      if str(var) == data.variable:
        variable_msg.variable = data.variable
        values = probs[var].getValues()
        cont = 0
        for i in values:
          state = StateWithProb()
          state.state = var.getStateName(cont)
          state.prob = i
          variable_msg.states.append(state)
          cont += 1
    return GetVarProbsResponse(variable_msg)

if __name__ == '__main__':
	
	rospy.init_node('openmarkov_ros_node', anonymous=False)
	n = OpenMarkovROS()
	try:
		rospy.spin()     	          
	except rospy.ROSInterruptException:
		pass