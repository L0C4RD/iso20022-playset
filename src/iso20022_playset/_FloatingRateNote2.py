# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISINOct2015Identifier
from . import Number

class FloatingRateNote2(base_types._BaseFieldType):

	__slots__ = ["_BsisPtSprd", "_RefRateIndx"]
	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if value is not None else base_types.UninitialisedField(self, 'BsisPtSprd', Number, False)

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = base_types.UninitialisedField(self, 'BsisPtSprd', Number, False)

	@property
	def RefRateIndx(self):
		return self._RefRateIndx

	@RefRateIndx.setter
	def RefRateIndx(self, value):
		self._RefRateIndx = value if value is not None else base_types.UninitialisedField(self, 'RefRateIndx', ISINOct2015Identifier, False)

	@RefRateIndx.deleter
	def RefRateIndx(self):
		del self._RefRateIndx
		self._RefRateIndx = base_types.UninitialisedField(self, 'RefRateIndx', ISINOct2015Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPtSprd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefRateIndx', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))