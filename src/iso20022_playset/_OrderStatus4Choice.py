from . import base_types
from ._InRepairStatusReason4Choice import InRepairStatusReason4Choice
from ._SuspendedStatusReason4Choice import SuspendedStatusReason4Choice
from ._OrderStatus4Code import OrderStatus4Code
from ._ConditionallyAcceptedStatus3Choice import ConditionallyAcceptedStatus3Choice
from ._CancelledStatusReason16 import CancelledStatusReason16
from ._RejectedStatus9 import RejectedStatus9
from ._PartiallySettledStatus10 import PartiallySettledStatus10

class OrderStatus4Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtlySttld", "_InRpr", "_Sspd", "_CondlyAccptd", "_Sts", "_Canc", "_Rjctd"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if type(value) != base_types.auto else self.make_default("Canc")

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = None

	@property
	def CondlyAccptd(self):
		return self._CondlyAccptd

	@CondlyAccptd.setter
	def CondlyAccptd(self, value):
		self._CondlyAccptd = value if type(value) != base_types.auto else self.make_default("CondlyAccptd")

	@CondlyAccptd.deleter
	def CondlyAccptd(self):
		del self._CondlyAccptd
		self._CondlyAccptd = None

	@property
	def InRpr(self):
		return self._InRpr

	@InRpr.setter
	def InRpr(self, value):
		self._InRpr = value if type(value) != base_types.auto else self.make_default("InRpr")

	@InRpr.deleter
	def InRpr(self):
		del self._InRpr
		self._InRpr = None

	@property
	def PrtlySttld(self):
		return self._PrtlySttld

	@PrtlySttld.setter
	def PrtlySttld(self, value):
		self._PrtlySttld = value if type(value) != base_types.auto else self.make_default("PrtlySttld")

	@PrtlySttld.deleter
	def PrtlySttld(self):
		del self._PrtlySttld
		self._PrtlySttld = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def Sspd(self):
		return self._Sspd

	@Sspd.setter
	def Sspd(self, value):
		self._Sspd = value if type(value) != base_types.auto else self.make_default("Sspd")

	@Sspd.deleter
	def Sspd(self):
		del self._Sspd
		self._Sspd = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancelledStatusReason16, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CondlyAccptd', type=ConditionallyAcceptedStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InRpr', type=InRepairStatusReason4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtlySttld', type=PartiallySettledStatus10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus9, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Sspd', type=SuspendedStatusReason4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sts', type=OrderStatus4Code, min=0, max=1, mutex_group=1, array=False),
	))

