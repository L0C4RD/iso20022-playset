# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InformationQualify1Code
from . import InputResultData6
from . import SaleCapabilities2Code

class InputResult6(base_types._BaseFieldType):

	__slots__ = ["_DvcTp", "_InfQlfr", "_InptRsltData"]
	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if value is not None else base_types.UninitialisedField(self, 'DvcTp', SaleCapabilities2Code, False)

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = base_types.UninitialisedField(self, 'DvcTp', SaleCapabilities2Code, False)

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if value is not None else base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@property
	def InptRsltData(self):
		return self._InptRsltData

	@InptRsltData.setter
	def InptRsltData(self, value):
		self._InptRsltData = value if value is not None else base_types.UninitialisedField(self, 'InptRsltData', InputResultData6, False)

	@InptRsltData.deleter
	def InptRsltData(self):
		del self._InptRsltData
		self._InptRsltData = base_types.UninitialisedField(self, 'InptRsltData', InputResultData6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvcTp', type=SaleCapabilities2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptRsltData', type=InputResultData6, min=1, max=1, mutex_group=None, array=False),
	))