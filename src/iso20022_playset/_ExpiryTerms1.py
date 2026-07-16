# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AutoExtension1
from . import DateAndDateTimeChoice
from . import Max2000Text
from . import YesNoIndicator

class ExpiryTerms1(base_types._BaseFieldType):

	__slots__ = ["_AutoXtnsn", "_Cond", "_DtTm", "_OpnEnddInd"]
	@property
	def AutoXtnsn(self):
		return self._AutoXtnsn

	@AutoXtnsn.setter
	def AutoXtnsn(self, value):
		self._AutoXtnsn = value if value is not None else base_types.UninitialisedField(self, 'AutoXtnsn', AutoExtension1, False)

	@AutoXtnsn.deleter
	def AutoXtnsn(self):
		del self._AutoXtnsn
		self._AutoXtnsn = base_types.UninitialisedField(self, 'AutoXtnsn', AutoExtension1, False)

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if value is not None else base_types.UninitialisedField(self, 'Cond', Max2000Text, False)

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = base_types.UninitialisedField(self, 'Cond', Max2000Text, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', DateAndDateTimeChoice, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', DateAndDateTimeChoice, False)

	@property
	def OpnEnddInd(self):
		return self._OpnEnddInd

	@OpnEnddInd.setter
	def OpnEnddInd(self, value):
		self._OpnEnddInd = value if value is not None else base_types.UninitialisedField(self, 'OpnEnddInd', YesNoIndicator, False)

	@OpnEnddInd.deleter
	def OpnEnddInd(self):
		del self._OpnEnddInd
		self._OpnEnddInd = base_types.UninitialisedField(self, 'OpnEnddInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutoXtnsn', type=AutoExtension1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cond', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnEnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))