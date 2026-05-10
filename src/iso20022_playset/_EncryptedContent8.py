from . import base_types
from ._AlgorithmIdentification25 import AlgorithmIdentification25
from ._ContentType2Code import ContentType2Code
from ._EncryptedDataElement2 import EncryptedDataElement2

class EncryptedContent8(base_types._BaseFieldType):

	__slots__ = ["_CnttNcrptnAlgo", "_CnttTp", "_NcrptdDataElmt"]
	@property
	def CnttNcrptnAlgo(self):
		return self._CnttNcrptnAlgo

	@CnttNcrptnAlgo.setter
	def CnttNcrptnAlgo(self, value):
		self._CnttNcrptnAlgo = value if type(value) != base_types.auto else self.make_default("CnttNcrptnAlgo")

	@CnttNcrptnAlgo.deleter
	def CnttNcrptnAlgo(self):
		del self._CnttNcrptnAlgo
		self._CnttNcrptnAlgo = None

	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if type(value) != base_types.auto else self.make_default("CnttTp")

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = None

	@property
	def NcrptdDataElmt(self):
		return self._NcrptdDataElmt

	@NcrptdDataElmt.setter
	def NcrptdDataElmt(self, value):
		self._NcrptdDataElmt = value if type(value) != base_types.auto else self.make_default("NcrptdDataElmt")

	@NcrptdDataElmt.deleter
	def NcrptdDataElmt(self):
		del self._NcrptdDataElmt
		self._NcrptdDataElmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttNcrptnAlgo', type=AlgorithmIdentification25, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdDataElmt', type=EncryptedDataElement2, min=1, max=None, mutex_group=None, array=True),
	))

