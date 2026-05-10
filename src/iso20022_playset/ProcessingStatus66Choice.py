from . import base_types
import CancellationStatus14Choice
import RejectionOrRepairStatus38Choice
import ProprietaryStatusAndReason6
import AcknowledgedAcceptedStatus21Choice

class ProcessingStatus66Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Prtry", "_Rpr", "_Canc"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

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

	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if type(value) != auto else self.make_default("Rpr")

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RejectionOrRepairStatus38Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus14Choice, min=0, max=1, mutex_group=1, array=False),
	))

