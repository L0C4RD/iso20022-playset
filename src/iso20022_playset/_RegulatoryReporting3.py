# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RegulatoryAuthority2
from . import RegulatoryReportingType1Code
from . import StructuredRegulatoryReporting3

class RegulatoryReporting3(base_types._BaseFieldType):

	__slots__ = ["_Authrty", "_DbtCdtRptgInd", "_Dtls"]
	@property
	def Authrty(self):
		return self._Authrty

	@Authrty.setter
	def Authrty(self, value):
		self._Authrty = value if value is not None else base_types.UninitialisedField(self, 'Authrty', RegulatoryAuthority2, False)

	@Authrty.deleter
	def Authrty(self):
		del self._Authrty
		self._Authrty = base_types.UninitialisedField(self, 'Authrty', RegulatoryAuthority2, False)

	@property
	def DbtCdtRptgInd(self):
		return self._DbtCdtRptgInd

	@DbtCdtRptgInd.setter
	def DbtCdtRptgInd(self, value):
		self._DbtCdtRptgInd = value if value is not None else base_types.UninitialisedField(self, 'DbtCdtRptgInd', RegulatoryReportingType1Code, False)

	@DbtCdtRptgInd.deleter
	def DbtCdtRptgInd(self):
		del self._DbtCdtRptgInd
		self._DbtCdtRptgInd = base_types.UninitialisedField(self, 'DbtCdtRptgInd', RegulatoryReportingType1Code, False)

	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if value is not None else base_types.UninitialisedField(self, 'Dtls', StructuredRegulatoryReporting3, True)

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = base_types.UninitialisedField(self, 'Dtls', StructuredRegulatoryReporting3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authrty', type=RegulatoryAuthority2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtCdtRptgInd', type=RegulatoryReportingType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dtls', type=StructuredRegulatoryReporting3, min=0, max=None, mutex_group=None, array=True),
	))