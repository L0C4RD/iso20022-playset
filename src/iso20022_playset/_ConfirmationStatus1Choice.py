from . import base_types
from ._ConfirmationRejectedStatus2 import ConfirmationRejectedStatus2
from ._OrderConfirmationStatus1Code import OrderConfirmationStatus1Code

class ConfirmationStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_AmdmntRjctd", "_ConfRjctd", "_Sts"]
	@property
	def AmdmntRjctd(self):
		return self._AmdmntRjctd

	@AmdmntRjctd.setter
	def AmdmntRjctd(self, value):
		self._AmdmntRjctd = value if type(value) != base_types.auto else self.make_default("AmdmntRjctd")

	@AmdmntRjctd.deleter
	def AmdmntRjctd(self):
		del self._AmdmntRjctd
		self._AmdmntRjctd = None

	@property
	def ConfRjctd(self):
		return self._ConfRjctd

	@ConfRjctd.setter
	def ConfRjctd(self, value):
		self._ConfRjctd = value if type(value) != base_types.auto else self.make_default("ConfRjctd")

	@ConfRjctd.deleter
	def ConfRjctd(self):
		del self._ConfRjctd
		self._ConfRjctd = None

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
		base_types.FieldEntry(name='AmdmntRjctd', type=ConfirmationRejectedStatus2, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='ConfRjctd', type=ConfirmationRejectedStatus2, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Sts', type=OrderConfirmationStatus1Code, min=0, max=1, mutex_group=1, array=False),
	))

