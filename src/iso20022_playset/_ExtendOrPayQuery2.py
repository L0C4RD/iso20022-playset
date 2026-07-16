# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Demand4
from . import DemandStatus1Code
from . import Undertaking9

class ExtendOrPayQuery2(base_types._BaseFieldType):

	__slots__ = ["_DmndDtls", "_Sts", "_UdrtkgId"]
	@property
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if value is not None else base_types.UninitialisedField(self, 'DmndDtls', Demand4, False)

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = base_types.UninitialisedField(self, 'DmndDtls', Demand4, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', DemandStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', DemandStatus1Code, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmndDtls', type=Demand4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=DemandStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))