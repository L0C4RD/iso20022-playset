# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max9NumericText import Max9NumericText
from ._Number import Number
from ._TimeUnit1Code import TimeUnit1Code

class ProcessTiming5(base_types._BaseFieldType):

	__slots__ = ["_EndTm", "_MaxNb", "_Prd", "_StartTm", "_UnitOfTm", "_WtgTm"]
	@property
	def EndTm(self):
		return self._EndTm

	@EndTm.setter
	def EndTm(self, value):
		self._EndTm = value if type(value) != base_types.auto else self.make_default("EndTm")

	@EndTm.deleter
	def EndTm(self):
		del self._EndTm
		self._EndTm = None

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if type(value) != base_types.auto else self.make_default("MaxNb")

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def StartTm(self):
		return self._StartTm

	@StartTm.setter
	def StartTm(self, value):
		self._StartTm = value if type(value) != base_types.auto else self.make_default("StartTm")

	@StartTm.deleter
	def StartTm(self):
		del self._StartTm
		self._StartTm = None

	@property
	def UnitOfTm(self):
		return self._UnitOfTm

	@UnitOfTm.setter
	def UnitOfTm(self, value):
		self._UnitOfTm = value if type(value) != base_types.auto else self.make_default("UnitOfTm")

	@UnitOfTm.deleter
	def UnitOfTm(self):
		del self._UnitOfTm
		self._UnitOfTm = None

	@property
	def WtgTm(self):
		return self._WtgTm

	@WtgTm.setter
	def WtgTm(self, value):
		self._WtgTm = value if type(value) != base_types.auto else self.make_default("WtgTm")

	@WtgTm.deleter
	def WtgTm(self):
		del self._WtgTm
		self._WtgTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfTm', type=TimeUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WtgTm', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
	))