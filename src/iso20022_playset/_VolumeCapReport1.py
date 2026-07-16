# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MICIdentifier
from . import Period4Choice
from . import VolumeCapReport2

class VolumeCapReport1(base_types._BaseFieldType):

	__slots__ = ["_InstrmRpt", "_RptgPrd", "_TradgVn"]
	@property
	def InstrmRpt(self):
		return self._InstrmRpt

	@InstrmRpt.setter
	def InstrmRpt(self, value):
		self._InstrmRpt = value if value is not None else base_types.UninitialisedField(self, 'InstrmRpt', VolumeCapReport2, True)

	@InstrmRpt.deleter
	def InstrmRpt(self):
		del self._InstrmRpt
		self._InstrmRpt = base_types.UninitialisedField(self, 'InstrmRpt', VolumeCapReport2, True)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', Period4Choice, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrmRpt', type=VolumeCapReport2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))