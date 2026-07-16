# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification25
from . import ContentType2Code
from . import EncryptedDataElement2

class EncryptedContent8(base_types._BaseFieldType):

	__slots__ = ["_CnttNcrptnAlgo", "_CnttTp", "_NcrptdDataElmt"]
	@property
	def CnttNcrptnAlgo(self):
		return self._CnttNcrptnAlgo

	@CnttNcrptnAlgo.setter
	def CnttNcrptnAlgo(self, value):
		self._CnttNcrptnAlgo = value if value is not None else base_types.UninitialisedField(self, 'CnttNcrptnAlgo', AlgorithmIdentification25, False)

	@CnttNcrptnAlgo.deleter
	def CnttNcrptnAlgo(self):
		del self._CnttNcrptnAlgo
		self._CnttNcrptnAlgo = base_types.UninitialisedField(self, 'CnttNcrptnAlgo', AlgorithmIdentification25, False)

	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if value is not None else base_types.UninitialisedField(self, 'CnttTp', ContentType2Code, False)

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = base_types.UninitialisedField(self, 'CnttTp', ContentType2Code, False)

	@property
	def NcrptdDataElmt(self):
		return self._NcrptdDataElmt

	@NcrptdDataElmt.setter
	def NcrptdDataElmt(self, value):
		self._NcrptdDataElmt = value if value is not None else base_types.UninitialisedField(self, 'NcrptdDataElmt', EncryptedDataElement2, True)

	@NcrptdDataElmt.deleter
	def NcrptdDataElmt(self):
		del self._NcrptdDataElmt
		self._NcrptdDataElmt = base_types.UninitialisedField(self, 'NcrptdDataElmt', EncryptedDataElement2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttNcrptnAlgo', type=AlgorithmIdentification25, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdDataElmt', type=EncryptedDataElement2, min=1, max=None, mutex_group=None, array=True),
	))