from . import base_types
from .RegulatoryReportingType1Code import RegulatoryReportingType1Code
from .StructuredRegulatoryReporting3 import StructuredRegulatoryReporting3
from .RegulatoryAuthority2 import RegulatoryAuthority2

class RegulatoryReporting3(base_types._BaseFieldType):

	__slots__ = ["_DbtCdtRptgInd", "_Dtls", "_Authrty"]
	@property
	def DbtCdtRptgInd(self):
		return self._DbtCdtRptgInd

	@DbtCdtRptgInd.setter
	def DbtCdtRptgInd(self, value):
		self._DbtCdtRptgInd = value if type(value) != base_types.auto else self.make_default("DbtCdtRptgInd")

	@DbtCdtRptgInd.deleter
	def DbtCdtRptgInd(self):
		del self._DbtCdtRptgInd
		self._DbtCdtRptgInd = None

	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if type(value) != base_types.auto else self.make_default("Dtls")

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = None

	@property
	def Authrty(self):
		return self._Authrty

	@Authrty.setter
	def Authrty(self, value):
		self._Authrty = value if type(value) != base_types.auto else self.make_default("Authrty")

	@Authrty.deleter
	def Authrty(self):
		del self._Authrty
		self._Authrty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtCdtRptgInd', type=RegulatoryReportingType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dtls', type=StructuredRegulatoryReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Authrty', type=RegulatoryAuthority2, min=0, max=1, mutex_group=None, array=False),
	))

