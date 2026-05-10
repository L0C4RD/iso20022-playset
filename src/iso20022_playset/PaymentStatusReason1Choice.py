import base_types
import UnmatchedStatusReason1Code
import Max35Text
import PendingSettlement2Code
import CancelledStatusReason1Code
import ProprietaryStatusJustification2
import SuspendedStatusReason1Code
import PendingFailingSettlement1Code

class PaymentStatusReason1Choice(base_types._BaseFieldType):

	__slots__ = ["_Sspd", "_Canc", "_Umtchd", "_PdgSttlm", "_PdgFlngSttlm", "_PrtryRjctn", "_Prtry"]
	@property
	def Sspd(self):
		return self._Sspd

	@Sspd.setter
	def Sspd(self, value):
		self._Sspd = value if type(value) != auto else self.make_default("Sspd")

	@Sspd.deleter
	def Sspd(self):
		del self._Sspd
		self._Sspd = None

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if type(value) != auto else self.make_default("Canc")

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = None

	@property
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if type(value) != auto else self.make_default("Umtchd")

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = None

	@property
	def PdgSttlm(self):
		return self._PdgSttlm

	@PdgSttlm.setter
	def PdgSttlm(self, value):
		self._PdgSttlm = value if type(value) != auto else self.make_default("PdgSttlm")

	@PdgSttlm.deleter
	def PdgSttlm(self):
		del self._PdgSttlm
		self._PdgSttlm = None

	@property
	def PdgFlngSttlm(self):
		return self._PdgFlngSttlm

	@PdgFlngSttlm.setter
	def PdgFlngSttlm(self, value):
		self._PdgFlngSttlm = value if type(value) != auto else self.make_default("PdgFlngSttlm")

	@PdgFlngSttlm.deleter
	def PdgFlngSttlm(self):
		del self._PdgFlngSttlm
		self._PdgFlngSttlm = None

	@property
	def PrtryRjctn(self):
		return self._PrtryRjctn

	@PrtryRjctn.setter
	def PrtryRjctn(self, value):
		self._PrtryRjctn = value if type(value) != auto else self.make_default("PrtryRjctn")

	@PrtryRjctn.deleter
	def PrtryRjctn(self):
		del self._PrtryRjctn
		self._PrtryRjctn = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sspd', type=SuspendedStatusReason1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancelledStatusReason1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=UnmatchedStatusReason1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSttlm', type=PendingSettlement2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgFlngSttlm', type=PendingFailingSettlement1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryRjctn', type=ProprietaryStatusJustification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

