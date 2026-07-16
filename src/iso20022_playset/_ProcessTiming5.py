# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max9NumericText
from . import Number
from . import TimeUnit1Code

class ProcessTiming5(base_types._BaseFieldType):

	__slots__ = ["_EndTm", "_MaxNb", "_Prd", "_StartTm", "_UnitOfTm", "_WtgTm"]
	@property
	def EndTm(self):
		return self._EndTm

	@EndTm.setter
	def EndTm(self, value):
		self._EndTm = value if value is not None else base_types.UninitialisedField(self, 'EndTm', ISODateTime, False)

	@EndTm.deleter
	def EndTm(self):
		del self._EndTm
		self._EndTm = base_types.UninitialisedField(self, 'EndTm', ISODateTime, False)

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
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', Max9NumericText, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', Max9NumericText, False)

	@property
	def StartTm(self):
		return self._StartTm

	@StartTm.setter
	def StartTm(self, value):
		self._StartTm = value if value is not None else base_types.UninitialisedField(self, 'StartTm', ISODateTime, False)

	@StartTm.deleter
	def StartTm(self):
		del self._StartTm
		self._StartTm = base_types.UninitialisedField(self, 'StartTm', ISODateTime, False)

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

	@property
	def WtgTm(self):
		return self._WtgTm

	@WtgTm.setter
	def WtgTm(self, value):
		self._WtgTm = value if value is not None else base_types.UninitialisedField(self, 'WtgTm', Max9NumericText, False)

	@WtgTm.deleter
	def WtgTm(self):
		del self._WtgTm
		self._WtgTm = base_types.UninitialisedField(self, 'WtgTm', Max9NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfTm', type=TimeUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WtgTm', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
	))