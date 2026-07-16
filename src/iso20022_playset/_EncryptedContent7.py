# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification32
from . import ContentType2Code
from . import Max100KBinary

class EncryptedContent7(base_types._BaseFieldType):

	__slots__ = ["_CnttNcrptnAlgo", "_CnttTp", "_NcrptdData"]
	@property
	def CnttNcrptnAlgo(self):
		return self._CnttNcrptnAlgo

	@CnttNcrptnAlgo.setter
	def CnttNcrptnAlgo(self, value):
		self._CnttNcrptnAlgo = value if value is not None else base_types.UninitialisedField(self, 'CnttNcrptnAlgo', AlgorithmIdentification32, False)

	@CnttNcrptnAlgo.deleter
	def CnttNcrptnAlgo(self):
		del self._CnttNcrptnAlgo
		self._CnttNcrptnAlgo = base_types.UninitialisedField(self, 'CnttNcrptnAlgo', AlgorithmIdentification32, False)

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
	def NcrptdData(self):
		return self._NcrptdData

	@NcrptdData.setter
	def NcrptdData(self, value):
		self._NcrptdData = value if value is not None else base_types.UninitialisedField(self, 'NcrptdData', Max100KBinary, False)

	@NcrptdData.deleter
	def NcrptdData(self):
		del self._NcrptdData
		self._NcrptdData = base_types.UninitialisedField(self, 'NcrptdData', Max100KBinary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttNcrptnAlgo', type=AlgorithmIdentification32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdData', type=Max100KBinary, min=1, max=1, mutex_group=None, array=False),
	))