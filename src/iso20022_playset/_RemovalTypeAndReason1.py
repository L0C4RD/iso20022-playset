# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateOrDateTimePeriod3Choice
from . import GenericIdentification30
from . import Removal1Choice

class RemovalTypeAndReason1(base_types._BaseFieldType):

	__slots__ = ["_ExclsnPrd", "_RmvlTp", "_Rsn"]
	@property
	def ExclsnPrd(self):
		return self._ExclsnPrd

	@ExclsnPrd.setter
	def ExclsnPrd(self, value):
		self._ExclsnPrd = value if value is not None else base_types.UninitialisedField(self, 'ExclsnPrd', DateOrDateTimePeriod3Choice, False)

	@ExclsnPrd.deleter
	def ExclsnPrd(self):
		del self._ExclsnPrd
		self._ExclsnPrd = base_types.UninitialisedField(self, 'ExclsnPrd', DateOrDateTimePeriod3Choice, False)

	@property
	def RmvlTp(self):
		return self._RmvlTp

	@RmvlTp.setter
	def RmvlTp(self, value):
		self._RmvlTp = value if value is not None else base_types.UninitialisedField(self, 'RmvlTp', Removal1Choice, False)

	@RmvlTp.deleter
	def RmvlTp(self):
		del self._RmvlTp
		self._RmvlTp = base_types.UninitialisedField(self, 'RmvlTp', Removal1Choice, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', GenericIdentification30, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExclsnPrd', type=DateOrDateTimePeriod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvlTp', type=Removal1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
	))