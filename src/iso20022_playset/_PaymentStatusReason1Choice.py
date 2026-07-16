# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledStatusReason1Code
from . import Max35Text
from . import PendingFailingSettlement1Code
from . import PendingSettlement2Code
from . import ProprietaryStatusJustification2
from . import SuspendedStatusReason1Code
from . import UnmatchedStatusReason1Code

class PaymentStatusReason1Choice(base_types._BaseFieldType):

	__slots__ = ["_Canc", "_PdgFlngSttlm", "_PdgSttlm", "_Prtry", "_PrtryRjctn", "_Sspd", "_Umtchd"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancelledStatusReason1Code, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancelledStatusReason1Code, False)

	@property
	def PdgFlngSttlm(self):
		return self._PdgFlngSttlm

	@PdgFlngSttlm.setter
	def PdgFlngSttlm(self, value):
		self._PdgFlngSttlm = value if value is not None else base_types.UninitialisedField(self, 'PdgFlngSttlm', PendingFailingSettlement1Code, False)

	@PdgFlngSttlm.deleter
	def PdgFlngSttlm(self):
		del self._PdgFlngSttlm
		self._PdgFlngSttlm = base_types.UninitialisedField(self, 'PdgFlngSttlm', PendingFailingSettlement1Code, False)

	@property
	def PdgSttlm(self):
		return self._PdgSttlm

	@PdgSttlm.setter
	def PdgSttlm(self, value):
		self._PdgSttlm = value if value is not None else base_types.UninitialisedField(self, 'PdgSttlm', PendingSettlement2Code, False)

	@PdgSttlm.deleter
	def PdgSttlm(self):
		del self._PdgSttlm
		self._PdgSttlm = base_types.UninitialisedField(self, 'PdgSttlm', PendingSettlement2Code, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@property
	def PrtryRjctn(self):
		return self._PrtryRjctn

	@PrtryRjctn.setter
	def PrtryRjctn(self, value):
		self._PrtryRjctn = value if value is not None else base_types.UninitialisedField(self, 'PrtryRjctn', ProprietaryStatusJustification2, False)

	@PrtryRjctn.deleter
	def PrtryRjctn(self):
		del self._PrtryRjctn
		self._PrtryRjctn = base_types.UninitialisedField(self, 'PrtryRjctn', ProprietaryStatusJustification2, False)

	@property
	def Sspd(self):
		return self._Sspd

	@Sspd.setter
	def Sspd(self, value):
		self._Sspd = value if value is not None else base_types.UninitialisedField(self, 'Sspd', SuspendedStatusReason1Code, False)

	@Sspd.deleter
	def Sspd(self):
		del self._Sspd
		self._Sspd = base_types.UninitialisedField(self, 'Sspd', SuspendedStatusReason1Code, False)

	@property
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if value is not None else base_types.UninitialisedField(self, 'Umtchd', UnmatchedStatusReason1Code, False)

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = base_types.UninitialisedField(self, 'Umtchd', UnmatchedStatusReason1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancelledStatusReason1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgFlngSttlm', type=PendingFailingSettlement1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSttlm', type=PendingSettlement2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryRjctn', type=ProprietaryStatusJustification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sspd', type=SuspendedStatusReason1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=UnmatchedStatusReason1Code, min=0, max=1, mutex_group=1, array=False),
	))