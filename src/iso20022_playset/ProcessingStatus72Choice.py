import base_types
import ProprietaryStatusAndReason6
import Reason4
import Reason18Choice

class ProcessingStatus72Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmpltd", "_Rjctd", "_PdgPrcg", "_Prtry", "_AckdAccptd"]
	@property
	def Cmpltd(self):
		return self._Cmpltd

	@Cmpltd.setter
	def Cmpltd(self, value):
		self._Cmpltd = value if type(value) != auto else self.make_default("Cmpltd")

	@Cmpltd.deleter
	def Cmpltd(self):
		del self._Cmpltd
		self._Cmpltd = None

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
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if type(value) != auto else self.make_default("PdgPrcg")

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = None

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
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmpltd', type=Reason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=Reason18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=Reason18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=Reason4, min=0, max=1, mutex_group=1, array=False),
	))

