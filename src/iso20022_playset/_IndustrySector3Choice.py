# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ExternalIndustrySectorClassification1Code import ExternalIndustrySectorClassification1Code
from ._NACEDomain2025Identifier import NACEDomain2025Identifier

class IndustrySector3Choice(base_types._BaseFieldType):

	__slots__ = ["_NACETxnmySctr", "_RgltryTxnmySctr"]
	@property
	def NACETxnmySctr(self):
		return self._NACETxnmySctr

	@NACETxnmySctr.setter
	def NACETxnmySctr(self, value):
		self._NACETxnmySctr = value if type(value) != base_types.auto else self.make_default("NACETxnmySctr")

	@NACETxnmySctr.deleter
	def NACETxnmySctr(self):
		del self._NACETxnmySctr
		self._NACETxnmySctr = None

	@property
	def RgltryTxnmySctr(self):
		return self._RgltryTxnmySctr

	@RgltryTxnmySctr.setter
	def RgltryTxnmySctr(self, value):
		self._RgltryTxnmySctr = value if type(value) != base_types.auto else self.make_default("RgltryTxnmySctr")

	@RgltryTxnmySctr.deleter
	def RgltryTxnmySctr(self):
		del self._RgltryTxnmySctr
		self._RgltryTxnmySctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NACETxnmySctr', type=NACEDomain2025Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RgltryTxnmySctr', type=ExternalIndustrySectorClassification1Code, min=0, max=1, mutex_group=1, array=False),
	))