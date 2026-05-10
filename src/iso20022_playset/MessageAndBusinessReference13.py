import base_types
import AdditionalInformation25
import Account33
import FinancialInstrument63Choice
import TypeOfRequest1Choice
import Max35Text
import PartyIdentification139
import AdditionalReference10
import Intermediary48
import References68Choice

class MessageAndBusinessReference13(base_types._BaseFieldType):

	__slots__ = ["_ReqIssr", "_TrfRef", "_ClntRef", "_Instrm", "_QryInf", "_ReqRcpt", "_MstrRef", "_IntrmyInf", "_CxlRef", "_InvstmtAcctDtls", "_TpOfReq", "_Ref"]
	@property
	def ReqIssr(self):
		return self._ReqIssr

	@ReqIssr.setter
	def ReqIssr(self, value):
		self._ReqIssr = value if type(value) != auto else self.make_default("ReqIssr")

	@ReqIssr.deleter
	def ReqIssr(self):
		del self._ReqIssr
		self._ReqIssr = None

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if type(value) != auto else self.make_default("TrfRef")

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if type(value) != auto else self.make_default("Instrm")

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = None

	@property
	def QryInf(self):
		return self._QryInf

	@QryInf.setter
	def QryInf(self, value):
		self._QryInf = value if type(value) != auto else self.make_default("QryInf")

	@QryInf.deleter
	def QryInf(self):
		del self._QryInf
		self._QryInf = None

	@property
	def ReqRcpt(self):
		return self._ReqRcpt

	@ReqRcpt.setter
	def ReqRcpt(self, value):
		self._ReqRcpt = value if type(value) != auto else self.make_default("ReqRcpt")

	@ReqRcpt.deleter
	def ReqRcpt(self):
		del self._ReqRcpt
		self._ReqRcpt = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if type(value) != auto else self.make_default("CxlRef")

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def TpOfReq(self):
		return self._TpOfReq

	@TpOfReq.setter
	def TpOfReq(self, value):
		self._TpOfReq = value if type(value) != auto else self.make_default("TpOfReq")

	@TpOfReq.deleter
	def TpOfReq(self):
		del self._TpOfReq
		self._TpOfReq = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqIssr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument63Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryInf', type=AdditionalInformation25, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqRcpt', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=Account33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfReq', type=TypeOfRequest1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References68Choice, min=0, max=1, mutex_group=None, array=False),
	))

