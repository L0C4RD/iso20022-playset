# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

import os
import sys

import iso20022

def demo_1():

	"""
	1: Parse messages
	Messages can be parsed from a variety of sources
	"""

	# Parse from file.
	path_to_xml = os.path.join(".", "sample_msgs", "sample-pain-002-001-14.xml")
	isomsg = iso20022.parse_file(path_to_xml)
	print(type(isomsg))


	# Parse from string.
	xml_string = """
		<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.002.001.14">
			<CstmrPmtStsRpt>
				<GrpHdr>
					<MsgId>ABC123</MsgId>
					<CreDtTm>1970-01-01T12:00:00</CreDtTm>
				</GrpHdr>
				<OrgnlGrpInfAndSts>
					<OrgnlMsgId>XYZ456</OrgnlMsgId>
					<OrgnlMsgNmId>pain.001.001.03</OrgnlMsgNmId>
				</OrgnlGrpInfAndSts>
			</CstmrPmtStsRpt>
		</Document>
	"""
	isomsg = iso20022.parse_xml(xml_string)
	print(type(isomsg))


	# Parse from etree.
	import xml.etree.ElementTree as ET

	tree = ET.parse(path_to_xml)
	isomsg = iso20022.parse_etree(tree)
	print(type(isomsg))

	
	# Also works with defusedxml.
	import defusedxml.ElementTree as dxET

	tree = dxET.parse(path_to_xml)
	isomsg = iso20022.parse_etree(tree)
	print(type(isomsg))


	# Read specific fields
	print(isomsg.CstmrPmtStsRpt.GrpHdr.InitgPty.Nm.get())

def demo_2():

	"""
	2: Create and modify messages
	Messages can be created with user-supplied data, 
	or fields in existing messages can be modified:
	"""

	# Make from scratch.
	isomsg = iso20022.PAIN_002_001_14.Document("Document")

	isomsg.CstmrPmtStsRpt = iso20022.CustomerPaymentStatusReportV14("CstmrPmtStsRpt")
	isomsg.CstmrPmtStsRpt.GrpHdr = iso20022.GroupHeader128("GrpHdr")
	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts = iso20022.OriginalGroupHeader22("OrgnlGrpInfAndSts")

	isomsg.CstmrPmtStsRpt.GrpHdr.MsgId = iso20022.Max35Text("MsgId")
	isomsg.CstmrPmtStsRpt.GrpHdr.MsgId.set("Example header msgid")

	isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm = iso20022.ISODateTime("CreDtTm")
	isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm.set("1970-01-01T12:00:00")

	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId = iso20022.Max35Text("OrgnlMsgId")
	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId.set("Example original msgid")

	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId = iso20022.Max35Text("OrgnlMsgNmId")
	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId.set("pain.001.001.02")

	print(isomsg.to_xml())
	isomsg.validate()


	# Create using defaults.
	isomsg = iso20022.PAIN_002_001_14.Document("Document")

	isomsg.CstmrPmtStsRpt = iso20022.auto()
	isomsg.CstmrPmtStsRpt.GrpHdr = iso20022.auto()
	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts = iso20022.auto()

	isomsg.CstmrPmtStsRpt.GrpHdr.MsgId = iso20022.auto()
	isomsg.CstmrPmtStsRpt.GrpHdr.MsgId.set("Example header msgid")

	isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm = iso20022.auto()
	isomsg.CstmrPmtStsRpt.GrpHdr.CreDtTm.set("1970-01-01T12:00:00")

	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId = iso20022.auto()
	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgId.set("Example original msgid")

	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId = iso20022.auto()
	isomsg.CstmrPmtStsRpt.OrgnlGrpInfAndSts.OrgnlMsgNmId.set("pain.001.001.02")

	print(isomsg.to_xml())
	isomsg.validate()


	# Modify existing messages
	xml_string = """
		<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
			<RsltnOfInvstgtn>
				<Assgnmt>
					<Id>RES123</Id>
					<Assgnr>
						<Pty>
							<Nm>AssigningBank</Nm>
						</Pty>
					</Assgnr>
					<Assgne>
						<Pty>
							<Nm>ReceivingBank</Nm>
						</Pty>
					</Assgne>
					<CreDtTm>1970-01-01T12:00:00</CreDtTm>
				</Assgnmt>
				<Sts>
					<RjctdMod>
						<Prtry>
							ExampleString
						</Prtry>
					</RjctdMod>
				</Sts>
			</RsltnOfInvstgtn>
		</Document>
	"""
	isomsg = iso20022.parse_xml(xml_string)

	isomsg.validate()

	isomsg.RsltnOfInvstgtn.Sts.RjctdMod[0].Prtry.set("Some other string")

	print(isomsg.to_xml())




def demo_3():

	"""
	3: Validate messages
	Messages can be validated against the ISO20022 schema.
	"""

	# Validate messages.
	xml_string = """
		<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.029.001.13">
			<RsltnOfInvstgtn>
				<Assgnmt>
					<Id>RES123</Id>
					<Assgnr>
						<Pty>
							<Nm>AssigningBank</Nm>
						</Pty>
					</Assgnr>
					<Assgne>
						<Pty>
							<Nm>ReceivingBank</Nm>
						</Pty>
					</Assgne>
					<CreDtTm>1970-01-01T12:00:00</CreDtTm>
				</Assgnmt>
				<Sts>
					<RjctdMod>
						<Prtry>
							ExampleString
						</Prtry>
					</RjctdMod>
				</Sts>
			</RsltnOfInvstgtn>
		</Document>
	"""
	isomsg = iso20022.parse_xml(xml_string)
	isomsg.validate()


	# Can detect invalid messages
	isomsg.RsltnOfInvstgtn.Assgnmt.Id.set("A"*36) # This is a Max35Text field
	try:
		isomsg.validate()
	except iso20022.ValidateError as e:
		print(f"{str(e)}")


	# Can validate whole message, or just individual sections or entries
	isomsg.RsltnOfInvstgtn.Sts.validate()
	isomsg.RsltnOfInvstgtn.Sts.RjctdMod[0].Prtry.validate()


def demo_4():

	"""
	4: Generate sample messages
	Schema-compliant messages of a specified type can
	be generated with synthetic data.
	"""

	# Generate messages of a given type.
	isomsg = iso20022.TSMT_049_001_01.Document("Document")
	for _ in range(3):
		isomsg.generate()
		print(isomsg.to_xml())


def demo_5():

	"""
	5: Serialise and deserialise messages
	(coming soon!) 
	"""
	pass

if __name__ == "__main__":

	try:
		demo_number = sys.argv[1]
	except:
		demo_number = "all"

	if demo_number.lower() == "all":
		demo_1()
		demo_2()
		demo_3()
		demo_4()
	if demo_number == "1":
		demo_1()
	elif demo_number == "2":
		demo_2()
	elif demo_number == "3":
		demo_3()
	elif demo_number == "4":
		demo_4()
	else:
		print("Unknown demo id {demo_number}")