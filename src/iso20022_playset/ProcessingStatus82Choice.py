from . import base_types
import RejectionStatus33Choice
import PendingStatus56Choice
import ProprietaryReason4
import ProprietaryStatusAndReason6
import CancellationStatus29Choice

class ProcessingStatus82Choice(base_types._BaseFieldType):

	__slots__ = ["_PdgCxl", "_Futr", "_Prcd", "_CxlReq", "_Prtry", "_Rjctd", "_Canc"]
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
	def Futr(self):
		return self._Futr

	@Futr.setter
	def Futr(self, value):
		self._Futr = value if type(value) != auto else self.make_default("Futr")

	@Futr.deleter
	def Futr(self):
		del self._Futr
		self._Futr = None

	@property
	def Prcd(self):
		return self._Prcd

	@Prcd.setter
	def Prcd(self, value):
		self._Prcd = value if type(value) != auto else self.make_default("Prcd")

	@Prcd.deleter
	def Prcd(self):
		del self._Prcd
		self._Prcd = None

	@property
	def CxlReq(self):
		return self._CxlReq

	@CxlReq.setter
	def CxlReq(self, value):
		self._CxlReq = value if type(value) != auto else self.make_default("CxlReq")

	@CxlReq.deleter
	def CxlReq(self):
		del self._CxlReq
		self._CxlReq = None

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
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus56Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Futr', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prcd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReq', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus33Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus29Choice, min=0, max=1, mutex_group=1, array=False),
	))

