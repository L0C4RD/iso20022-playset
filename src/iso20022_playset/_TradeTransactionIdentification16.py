from . import base_types
from .Max52Text import Max52Text
from .Max140Text import Max140Text
from .OrganisationIdentification15Choice import OrganisationIdentification15Choice
from .PartyIdentification236Choice import PartyIdentification236Choice

class TradeTransactionIdentification16(base_types._BaseFieldType):

	__slots__ = ["_RptgCtrPty", "_CollPrtflId", "_NttyRspnsblForRpt", "_OthrCtrPty", "_TechRcrdId"]
	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != base_types.auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def CollPrtflId(self):
		return self._CollPrtflId

	@CollPrtflId.setter
	def CollPrtflId(self, value):
		self._CollPrtflId = value if type(value) != base_types.auto else self.make_default("CollPrtflId")

	@CollPrtflId.deleter
	def CollPrtflId(self):
		del self._CollPrtflId
		self._CollPrtflId = None

	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if type(value) != base_types.auto else self.make_default("NttyRspnsblForRpt")

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = None

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != base_types.auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgCtrPty', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrtflId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=PartyIdentification236Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

