import base_types
import ProprietaryReason4
import ProprietaryStatusAndReason6

class AllocationStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_FullyAllctd", "_Prtry", "_PrtlyAllctd"]
	@property
	def FullyAllctd(self):
		return self._FullyAllctd

	@FullyAllctd.setter
	def FullyAllctd(self, value):
		self._FullyAllctd = value if type(value) != auto else self.make_default("FullyAllctd")

	@FullyAllctd.deleter
	def FullyAllctd(self):
		del self._FullyAllctd
		self._FullyAllctd = None

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
	def PrtlyAllctd(self):
		return self._PrtlyAllctd

	@PrtlyAllctd.setter
	def PrtlyAllctd(self, value):
		self._PrtlyAllctd = value if type(value) != auto else self.make_default("PrtlyAllctd")

	@PrtlyAllctd.deleter
	def PrtlyAllctd(self):
		del self._PrtlyAllctd
		self._PrtlyAllctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullyAllctd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtlyAllctd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
	))

