from . import base_types
from .EncryptionFormat1Code import EncryptionFormat1Code
from .Algorithm11Code import Algorithm11Code
from .AlgorithmIdentification12 import AlgorithmIdentification12

class Parameter4(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_NcrptnFrmt", "_MskGnrtrAlgo"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != base_types.auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	@property
	def NcrptnFrmt(self):
		return self._NcrptnFrmt

	@NcrptnFrmt.setter
	def NcrptnFrmt(self, value):
		self._NcrptnFrmt = value if type(value) != base_types.auto else self.make_default("NcrptnFrmt")

	@NcrptnFrmt.deleter
	def NcrptnFrmt(self):
		del self._NcrptnFrmt
		self._NcrptnFrmt = None

	@property
	def MskGnrtrAlgo(self):
		return self._MskGnrtrAlgo

	@MskGnrtrAlgo.setter
	def MskGnrtrAlgo(self, value):
		self._MskGnrtrAlgo = value if type(value) != base_types.auto else self.make_default("MskGnrtrAlgo")

	@MskGnrtrAlgo.deleter
	def MskGnrtrAlgo(self):
		del self._MskGnrtrAlgo
		self._MskGnrtrAlgo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm11Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptnFrmt', type=EncryptionFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MskGnrtrAlgo', type=AlgorithmIdentification12, min=0, max=1, mutex_group=None, array=False),
	))

