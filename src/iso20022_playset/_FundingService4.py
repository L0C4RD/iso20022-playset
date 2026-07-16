# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundingSource5
from . import ISODateTime
from . import Max256Text
from . import Max35Text
from . import Max3Text
from . import Max500Text

class FundingService4(base_types._BaseFieldType):

	__slots__ = ["_BizPurp", "_ClmAssgnr", "_ClmCrdntls", "_Desc", "_DfrrdDtTm", "_FndgSrc", "_Nm", "_Prvdr", "_Ref", "_SvcPrcgTp"]
	@property
	def BizPurp(self):
		return self._BizPurp

	@BizPurp.setter
	def BizPurp(self, value):
		self._BizPurp = value if value is not None else base_types.UninitialisedField(self, 'BizPurp', Max500Text, False)

	@BizPurp.deleter
	def BizPurp(self):
		del self._BizPurp
		self._BizPurp = base_types.UninitialisedField(self, 'BizPurp', Max500Text, False)

	@property
	def ClmAssgnr(self):
		return self._ClmAssgnr

	@ClmAssgnr.setter
	def ClmAssgnr(self, value):
		self._ClmAssgnr = value if value is not None else base_types.UninitialisedField(self, 'ClmAssgnr', Max35Text, False)

	@ClmAssgnr.deleter
	def ClmAssgnr(self):
		del self._ClmAssgnr
		self._ClmAssgnr = base_types.UninitialisedField(self, 'ClmAssgnr', Max35Text, False)

	@property
	def ClmCrdntls(self):
		return self._ClmCrdntls

	@ClmCrdntls.setter
	def ClmCrdntls(self, value):
		self._ClmCrdntls = value if value is not None else base_types.UninitialisedField(self, 'ClmCrdntls', Max500Text, False)

	@ClmCrdntls.deleter
	def ClmCrdntls(self):
		del self._ClmCrdntls
		self._ClmCrdntls = base_types.UninitialisedField(self, 'ClmCrdntls', Max500Text, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@property
	def DfrrdDtTm(self):
		return self._DfrrdDtTm

	@DfrrdDtTm.setter
	def DfrrdDtTm(self, value):
		self._DfrrdDtTm = value if value is not None else base_types.UninitialisedField(self, 'DfrrdDtTm', ISODateTime, False)

	@DfrrdDtTm.deleter
	def DfrrdDtTm(self):
		del self._DfrrdDtTm
		self._DfrrdDtTm = base_types.UninitialisedField(self, 'DfrrdDtTm', ISODateTime, False)

	@property
	def FndgSrc(self):
		return self._FndgSrc

	@FndgSrc.setter
	def FndgSrc(self, value):
		self._FndgSrc = value if value is not None else base_types.UninitialisedField(self, 'FndgSrc', FundingSource5, True)

	@FndgSrc.deleter
	def FndgSrc(self):
		del self._FndgSrc
		self._FndgSrc = base_types.UninitialisedField(self, 'FndgSrc', FundingSource5, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if value is not None else base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def SvcPrcgTp(self):
		return self._SvcPrcgTp

	@SvcPrcgTp.setter
	def SvcPrcgTp(self, value):
		self._SvcPrcgTp = value if value is not None else base_types.UninitialisedField(self, 'SvcPrcgTp', Max3Text, False)

	@SvcPrcgTp.deleter
	def SvcPrcgTp(self):
		del self._SvcPrcgTp
		self._SvcPrcgTp = base_types.UninitialisedField(self, 'SvcPrcgTp', Max3Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizPurp', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClmCrdntls', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndgSrc', type=FundingSource5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcPrcgTp', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
	))