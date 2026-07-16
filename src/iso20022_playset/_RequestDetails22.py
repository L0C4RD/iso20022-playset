# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingChannel2Code
from . import GenericIdentification30
from . import LinkageType3Choice
from . import Linkages57
from . import PriorityNumeric4Choice
from . import References14
from . import YesNoIndicator

class RequestDetails22(base_types._BaseFieldType):

	__slots__ = ["_ClrChanl", "_Lkg", "_Lnkgs", "_OthrPrcg", "_PrtlSttlmInd", "_Prty", "_Ref"]
	@property
	def ClrChanl(self):
		return self._ClrChanl

	@ClrChanl.setter
	def ClrChanl(self, value):
		self._ClrChanl = value if value is not None else base_types.UninitialisedField(self, 'ClrChanl', ClearingChannel2Code, False)

	@ClrChanl.deleter
	def ClrChanl(self):
		del self._ClrChanl
		self._ClrChanl = base_types.UninitialisedField(self, 'ClrChanl', ClearingChannel2Code, False)

	@property
	def Lkg(self):
		return self._Lkg

	@Lkg.setter
	def Lkg(self, value):
		self._Lkg = value if value is not None else base_types.UninitialisedField(self, 'Lkg', LinkageType3Choice, False)

	@Lkg.deleter
	def Lkg(self):
		del self._Lkg
		self._Lkg = base_types.UninitialisedField(self, 'Lkg', LinkageType3Choice, False)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@property
	def OthrPrcg(self):
		return self._OthrPrcg

	@OthrPrcg.setter
	def OthrPrcg(self, value):
		self._OthrPrcg = value if value is not None else base_types.UninitialisedField(self, 'OthrPrcg', GenericIdentification30, True)

	@OthrPrcg.deleter
	def OthrPrcg(self):
		del self._OthrPrcg
		self._OthrPrcg = base_types.UninitialisedField(self, 'OthrPrcg', GenericIdentification30, True)

	@property
	def PrtlSttlmInd(self):
		return self._PrtlSttlmInd

	@PrtlSttlmInd.setter
	def PrtlSttlmInd(self, value):
		self._PrtlSttlmInd = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlmInd', YesNoIndicator, False)

	@PrtlSttlmInd.deleter
	def PrtlSttlmInd(self):
		del self._PrtlSttlmInd
		self._PrtlSttlmInd = base_types.UninitialisedField(self, 'PrtlSttlmInd', YesNoIndicator, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References14, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrChanl', type=ClearingChannel2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lkg', type=LinkageType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrPrcg', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlSttlmInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References14, min=1, max=1, mutex_group=None, array=False),
	))