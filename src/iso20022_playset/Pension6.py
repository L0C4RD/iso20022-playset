from . import base_types
from .Max35Text import Max35Text
from .AdditionalInformation15 import AdditionalInformation15
from .YesNoIndicator import YesNoIndicator
from .PensionTransferScope1Choice import PensionTransferScope1Choice
from .PensionSchemeType3Choice import PensionSchemeType3Choice
from .PensionPolicy1 import PensionPolicy1
from .TaxReference1 import TaxReference1

class Pension6(base_types._BaseFieldType):

	__slots__ = ["_TrfScp", "_DrwdwnTrchId", "_Id", "_NonWrpprTrf", "_Tp", "_TaxRef", "_AddtlInf"]
	@property
	def TrfScp(self):
		return self._TrfScp

	@TrfScp.setter
	def TrfScp(self, value):
		self._TrfScp = value if type(value) != auto else self.make_default("TrfScp")

	@TrfScp.deleter
	def TrfScp(self):
		del self._TrfScp
		self._TrfScp = None

	@property
	def DrwdwnTrchId(self):
		return self._DrwdwnTrchId

	@DrwdwnTrchId.setter
	def DrwdwnTrchId(self, value):
		self._DrwdwnTrchId = value if type(value) != auto else self.make_default("DrwdwnTrchId")

	@DrwdwnTrchId.deleter
	def DrwdwnTrchId(self):
		del self._DrwdwnTrchId
		self._DrwdwnTrchId = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def NonWrpprTrf(self):
		return self._NonWrpprTrf

	@NonWrpprTrf.setter
	def NonWrpprTrf(self, value):
		self._NonWrpprTrf = value if type(value) != auto else self.make_default("NonWrpprTrf")

	@NonWrpprTrf.deleter
	def NonWrpprTrf(self):
		del self._NonWrpprTrf
		self._NonWrpprTrf = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TaxRef(self):
		return self._TaxRef

	@TaxRef.setter
	def TaxRef(self, value):
		self._TaxRef = value if type(value) != auto else self.make_default("TaxRef")

	@TaxRef.deleter
	def TaxRef(self):
		del self._TaxRef
		self._TaxRef = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrfScp', type=PensionTransferScope1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnTrchId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PensionPolicy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonWrpprTrf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PensionSchemeType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRef', type=TaxReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

