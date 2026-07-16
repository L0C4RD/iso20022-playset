# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number

class TimeFrame8Choice(base_types._BaseFieldType):

	__slots__ = ["_RPlus", "_TPlus"]
	@property
	def RPlus(self):
		return self._RPlus

	@RPlus.setter
	def RPlus(self, value):
		self._RPlus = value if value is not None else base_types.UninitialisedField(self, 'RPlus', Number, False)

	@RPlus.deleter
	def RPlus(self):
		del self._RPlus
		self._RPlus = base_types.UninitialisedField(self, 'RPlus', Number, False)

	@property
	def TPlus(self):
		return self._TPlus

	@TPlus.setter
	def TPlus(self, value):
		self._TPlus = value if value is not None else base_types.UninitialisedField(self, 'TPlus', Number, False)

	@TPlus.deleter
	def TPlus(self):
		del self._TPlus
		self._TPlus = base_types.UninitialisedField(self, 'TPlus', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RPlus', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TPlus', type=Number, min=0, max=1, mutex_group=1, array=False),
	))