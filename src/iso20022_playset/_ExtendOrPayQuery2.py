from . import base_types
from ._Demand4 import Demand4
from ._DemandStatus1Code import DemandStatus1Code
from ._Undertaking9 import Undertaking9

class ExtendOrPayQuery2(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgId", "_DmndDtls", "_Sts"]
	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != base_types.auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	@property
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if type(value) != base_types.auto else self.make_default("DmndDtls")

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = None

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
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDtls', type=Demand4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=DemandStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

