import base_types
import ProprietaryStatusAndReason6
import PendingCancellationStatus14Choice
import NoSpecifiedReason1
import RejectedStatus38Choice
import CancelledStatus11Choice

class MarketClaimCancellationRequestStatus2Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_Rjctd", "_PdgCxl", "_CxlCmpltd", "_PrtrySts"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if type(value) != auto else self.make_default("Accptd")

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if type(value) != auto else self.make_default("PdgCxl")

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = None

	@property
	def CxlCmpltd(self):
		return self._CxlCmpltd

	@CxlCmpltd.setter
	def CxlCmpltd(self, value):
		self._CxlCmpltd = value if type(value) != auto else self.make_default("CxlCmpltd")

	@CxlCmpltd.deleter
	def CxlCmpltd(self):
		del self._CxlCmpltd
		self._CxlCmpltd = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=NoSpecifiedReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus38Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingCancellationStatus14Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlCmpltd', type=CancelledStatus11Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
	))

