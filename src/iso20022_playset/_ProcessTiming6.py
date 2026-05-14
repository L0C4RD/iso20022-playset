# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max9NumericText import Max9NumericText
from ._TimeUnit1Code import TimeUnit1Code

class ProcessTiming6(base_types._BaseFieldType):

	__slots__ = ["_EndTm", "_Prd", "_StartTm", "_UnitOfTm"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfTm', type=TimeUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))