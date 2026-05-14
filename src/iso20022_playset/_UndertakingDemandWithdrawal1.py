# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Demand3 import Demand3
from ._Max35Text import Max35Text
from ._Undertaking6 import Undertaking6

class UndertakingDemandWithdrawal1(base_types._BaseFieldType):

	__slots__ = ["_AdvsgPtyRefNb", "_CnfrmrRefNb", "_DmndDtls", "_UdrtkgId"]
	@property
	def AdvsgPtyRefNb(self):
		return self._AdvsgPtyRefNb

	@AdvsgPtyRefNb.setter
	def AdvsgPtyRefNb(self, value):
		self._AdvsgPtyRefNb = value if type(value) != base_types.auto else self.make_default("AdvsgPtyRefNb")

	@AdvsgPtyRefNb.deleter
	def AdvsgPtyRefNb(self):
		del self._AdvsgPtyRefNb
		self._AdvsgPtyRefNb = None

	@property
	def CnfrmrRefNb(self):
		return self._CnfrmrRefNb

	@CnfrmrRefNb.setter
	def CnfrmrRefNb(self, value):
		self._CnfrmrRefNb = value if type(value) != base_types.auto else self.make_default("CnfrmrRefNb")

	@CnfrmrRefNb.deleter
	def CnfrmrRefNb(self):
		del self._CnfrmrRefNb
		self._CnfrmrRefNb = None

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
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != base_types.auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDtls', type=Demand3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking6, min=1, max=1, mutex_group=None, array=False),
	))