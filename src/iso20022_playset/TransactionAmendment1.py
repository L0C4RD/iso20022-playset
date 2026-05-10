import base_types
import Max2048Text
import TransactionAmendment1Choice

class TransactionAmendment1(base_types._BaseFieldType):

	__slots__ = ["_Rcrd", "_Pth"]
	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def Pth(self):
		return self._Pth

	@Pth.setter
	def Pth(self, value):
		self._Pth = value if type(value) != auto else self.make_default("Pth")

	@Pth.deleter
	def Pth(self):
		del self._Pth
		self._Pth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcrd', type=TransactionAmendment1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pth', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))

