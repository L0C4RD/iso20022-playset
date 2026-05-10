from . import base_types
from .Number import Number
from .Algorithm11Code import Algorithm11Code
from .AlgorithmIdentification12 import AlgorithmIdentification12

class Parameter8(base_types._BaseFieldType):

	__slots__ = ["_MskGnrtrAlgo", "_TrlrFld", "_DgstAlgo", "_SaltLngth"]
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

	@property
	def TrlrFld(self):
		return self._TrlrFld

	@TrlrFld.setter
	def TrlrFld(self, value):
		self._TrlrFld = value if type(value) != base_types.auto else self.make_default("TrlrFld")

	@TrlrFld.deleter
	def TrlrFld(self):
		del self._TrlrFld
		self._TrlrFld = None

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
	def SaltLngth(self):
		return self._SaltLngth

	@SaltLngth.setter
	def SaltLngth(self, value):
		self._SaltLngth = value if type(value) != base_types.auto else self.make_default("SaltLngth")

	@SaltLngth.deleter
	def SaltLngth(self):
		del self._SaltLngth
		self._SaltLngth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MskGnrtrAlgo', type=AlgorithmIdentification12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrFld', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm11Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaltLngth', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

