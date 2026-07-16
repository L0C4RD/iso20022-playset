# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max9NumericText
from . import Number
from . import TimeUnit1Code

class ProcessRetry3(base_types._BaseFieldType):

	__slots__ = ["_Dely", "_MaxNb", "_UnitOfTm"]
	@property
	def Dely(self):
		return self._Dely

	@Dely.setter
	def Dely(self, value):
		self._Dely = value if value is not None else base_types.UninitialisedField(self, 'Dely', Max9NumericText, False)

	@Dely.deleter
	def Dely(self):
		del self._Dely
		self._Dely = base_types.UninitialisedField(self, 'Dely', Max9NumericText, False)

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if value is not None else base_types.UninitialisedField(self, 'MaxNb', Number, False)

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = base_types.UninitialisedField(self, 'MaxNb', Number, False)

	@property
	def UnitOfTm(self):
		return self._UnitOfTm

	@UnitOfTm.setter
	def UnitOfTm(self, value):
		self._UnitOfTm = value if value is not None else base_types.UninitialisedField(self, 'UnitOfTm', TimeUnit1Code, False)

	@UnitOfTm.deleter
	def UnitOfTm(self):
		del self._UnitOfTm
		self._UnitOfTm = base_types.UninitialisedField(self, 'UnitOfTm', TimeUnit1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dely', type=Max9NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfTm', type=TimeUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))