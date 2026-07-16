# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import PositiveNumber

class OrderPriority1(base_types._BaseFieldType):

	__slots__ = ["_Sz", "_TmStmp"]
	@property
	def Sz(self):
		return self._Sz

	@Sz.setter
	def Sz(self, value):
		self._Sz = value if value is not None else base_types.UninitialisedField(self, 'Sz', PositiveNumber, False)

	@Sz.deleter
	def Sz(self):
		del self._Sz
		self._Sz = base_types.UninitialisedField(self, 'Sz', PositiveNumber, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sz', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))