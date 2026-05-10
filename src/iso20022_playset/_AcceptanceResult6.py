from . import base_types
from ._Max105Text import Max105Text
from ._MandateReason1Choice import MandateReason1Choice
from ._YesNoIndicator import YesNoIndicator

class AcceptanceResult6(base_types._BaseFieldType):

	__slots__ = ["_RjctRsn", "_Accptd", "_AddtlRjctRsnInf"]
	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if type(value) != base_types.auto else self.make_default("RjctRsn")

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = None

	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != base_types.auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

	@property
	def AddtlRjctRsnInf(self):
		return self._AddtlRjctRsnInf

	@AddtlRjctRsnInf.setter
	def AddtlRjctRsnInf(self, value):
		self._AddtlRjctRsnInf = value if type(value) != base_types.auto else self.make_default("AddtlRjctRsnInf")

	@AddtlRjctRsnInf.deleter
	def AddtlRjctRsnInf(self):
		del self._AddtlRjctRsnInf
		self._AddtlRjctRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctRsn', type=MandateReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Accptd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRjctRsnInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
	))

