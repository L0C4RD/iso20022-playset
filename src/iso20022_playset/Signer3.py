import base_types
import Number
import Recipient5Choice
import AlgorithmIdentification16
import Max3000Binary
import AlgorithmIdentification17

class Signer3(base_types._BaseFieldType):

	__slots__ = ["_SgnrId", "_Vrsn", "_Sgntr", "_DgstAlgo", "_SgntrAlgo"]
	@property
	def SgnrId(self):
		return self._SgnrId

	@SgnrId.setter
	def SgnrId(self, value):
		self._SgnrId = value if type(value) != auto else self.make_default("SgnrId")

	@SgnrId.deleter
	def SgnrId(self):
		del self._SgnrId
		self._SgnrId = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	@property
	def SgntrAlgo(self):
		return self._SgntrAlgo

	@SgntrAlgo.setter
	def SgntrAlgo(self, value):
		self._SgntrAlgo = value if type(value) != auto else self.make_default("SgntrAlgo")

	@SgntrAlgo.deleter
	def SgntrAlgo(self):
		del self._SgntrAlgo
		self._SgntrAlgo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgnrId', type=Recipient5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=Max3000Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstAlgo', type=AlgorithmIdentification16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrAlgo', type=AlgorithmIdentification17, min=1, max=1, mutex_group=None, array=False),
	))

