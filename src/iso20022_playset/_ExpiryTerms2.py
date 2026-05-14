# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AutoExtension1 import AutoExtension1
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._Max2000Text import Max2000Text
from ._YesNoIndicator import YesNoIndicator

class ExpiryTerms2(base_types._BaseFieldType):

	__slots__ = ["_AutoXtnsn", "_Cond", "_DtTm", "_OpnEnddInd"]
	@property
	def AutoXtnsn(self):
		return self._AutoXtnsn

	@AutoXtnsn.setter
	def AutoXtnsn(self, value):
		self._AutoXtnsn = value if type(value) != base_types.auto else self.make_default("AutoXtnsn")

	@AutoXtnsn.deleter
	def AutoXtnsn(self):
		del self._AutoXtnsn
		self._AutoXtnsn = None

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != base_types.auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != base_types.auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def OpnEnddInd(self):
		return self._OpnEnddInd

	@OpnEnddInd.setter
	def OpnEnddInd(self, value):
		self._OpnEnddInd = value if type(value) != base_types.auto else self.make_default("OpnEnddInd")

	@OpnEnddInd.deleter
	def OpnEnddInd(self):
		del self._OpnEnddInd
		self._OpnEnddInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutoXtnsn', type=AutoExtension1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnEnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))