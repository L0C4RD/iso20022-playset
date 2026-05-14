# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MetadataReport5 import MetadataReport5
from ._SupplementaryData1 import SupplementaryData1

class RegulatoryMetadataReportV01(base_types._BaseFieldType):

	__slots__ = ["_MetadataRpt", "_SplmtryData"]
	@property
	def MetadataRpt(self):
		return self._MetadataRpt

	@MetadataRpt.setter
	def MetadataRpt(self, value):
		self._MetadataRpt = value if type(value) != base_types.auto else self.make_default("MetadataRpt")

	@MetadataRpt.deleter
	def MetadataRpt(self):
		del self._MetadataRpt
		self._MetadataRpt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MetadataRpt', type=MetadataReport5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))