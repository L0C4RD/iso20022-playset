# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account33
from . import AdditionalInformation25
from . import AdditionalReference10
from . import FinancialInstrument63Choice
from . import Intermediary48
from . import Max35Text
from . import PartyIdentification139
from . import References68Choice
from . import TypeOfRequest1Choice

class MessageAndBusinessReference13(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_CxlRef", "_Instrm", "_IntrmyInf", "_InvstmtAcctDtls", "_MstrRef", "_QryInf", "_Ref", "_ReqIssr", "_ReqRcpt", "_TpOfReq", "_TrfRef"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if value is not None else base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@property
	def Instrm(self):
		return self._Instrm

	@Instrm.setter
	def Instrm(self, value):
		self._Instrm = value if value is not None else base_types.UninitialisedField(self, 'Instrm', FinancialInstrument63Choice, False)

	@Instrm.deleter
	def Instrm(self):
		del self._Instrm
		self._Instrm = base_types.UninitialisedField(self, 'Instrm', FinancialInstrument63Choice, False)

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInf', Intermediary48, True)

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = base_types.UninitialisedField(self, 'IntrmyInf', Intermediary48, True)

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', Account33, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', Account33, False)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def QryInf(self):
		return self._QryInf

	@QryInf.setter
	def QryInf(self, value):
		self._QryInf = value if value is not None else base_types.UninitialisedField(self, 'QryInf', AdditionalInformation25, True)

	@QryInf.deleter
	def QryInf(self):
		del self._QryInf
		self._QryInf = base_types.UninitialisedField(self, 'QryInf', AdditionalInformation25, True)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References68Choice, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References68Choice, False)

	@property
	def ReqIssr(self):
		return self._ReqIssr

	@ReqIssr.setter
	def ReqIssr(self, value):
		self._ReqIssr = value if value is not None else base_types.UninitialisedField(self, 'ReqIssr', PartyIdentification139, False)

	@ReqIssr.deleter
	def ReqIssr(self):
		del self._ReqIssr
		self._ReqIssr = base_types.UninitialisedField(self, 'ReqIssr', PartyIdentification139, False)

	@property
	def ReqRcpt(self):
		return self._ReqRcpt

	@ReqRcpt.setter
	def ReqRcpt(self, value):
		self._ReqRcpt = value if value is not None else base_types.UninitialisedField(self, 'ReqRcpt', PartyIdentification139, False)

	@ReqRcpt.deleter
	def ReqRcpt(self):
		del self._ReqRcpt
		self._ReqRcpt = base_types.UninitialisedField(self, 'ReqRcpt', PartyIdentification139, False)

	@property
	def TpOfReq(self):
		return self._TpOfReq

	@TpOfReq.setter
	def TpOfReq(self, value):
		self._TpOfReq = value if value is not None else base_types.UninitialisedField(self, 'TpOfReq', TypeOfRequest1Choice, False)

	@TpOfReq.deleter
	def TpOfReq(self):
		del self._TpOfReq
		self._TpOfReq = base_types.UninitialisedField(self, 'TpOfReq', TypeOfRequest1Choice, False)

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if value is not None else base_types.UninitialisedField(self, 'TrfRef', Max35Text, False)

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = base_types.UninitialisedField(self, 'TrfRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instrm', type=FinancialInstrument63Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=Account33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryInf', type=AdditionalInformation25, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=References68Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqIssr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRcpt', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfReq', type=TypeOfRequest1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))