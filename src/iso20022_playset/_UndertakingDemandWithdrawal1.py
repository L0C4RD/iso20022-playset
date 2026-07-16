# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Demand3
from . import Max35Text
from . import Undertaking6

class UndertakingDemandWithdrawal1(base_types._BaseFieldType):

	__slots__ = ["_AdvsgPtyRefNb", "_CnfrmrRefNb", "_DmndDtls", "_UdrtkgId"]
	@property
	def AdvsgPtyRefNb(self):
		return self._AdvsgPtyRefNb

	@AdvsgPtyRefNb.setter
	def AdvsgPtyRefNb(self, value):
		self._AdvsgPtyRefNb = value if value is not None else base_types.UninitialisedField(self, 'AdvsgPtyRefNb', Max35Text, False)

	@AdvsgPtyRefNb.deleter
	def AdvsgPtyRefNb(self):
		del self._AdvsgPtyRefNb
		self._AdvsgPtyRefNb = base_types.UninitialisedField(self, 'AdvsgPtyRefNb', Max35Text, False)

	@property
	def CnfrmrRefNb(self):
		return self._CnfrmrRefNb

	@CnfrmrRefNb.setter
	def CnfrmrRefNb(self, value):
		self._CnfrmrRefNb = value if value is not None else base_types.UninitialisedField(self, 'CnfrmrRefNb', Max35Text, False)

	@CnfrmrRefNb.deleter
	def CnfrmrRefNb(self):
		del self._CnfrmrRefNb
		self._CnfrmrRefNb = base_types.UninitialisedField(self, 'CnfrmrRefNb', Max35Text, False)

	@property
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if value is not None else base_types.UninitialisedField(self, 'DmndDtls', Demand3, False)

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = base_types.UninitialisedField(self, 'DmndDtls', Demand3, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking6, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDtls', type=Demand3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking6, min=1, max=1, mutex_group=None, array=False),
	))