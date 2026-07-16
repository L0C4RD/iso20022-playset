# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Number

class VariableInterest1Rate(base_types._BaseFieldType):

	__slots__ = ["_BsisPtSprd", "_Indx"]
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
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', Max35Text, False)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPtSprd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Indx', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))