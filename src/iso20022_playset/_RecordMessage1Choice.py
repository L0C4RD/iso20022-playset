# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2MBBinary

class RecordMessage1Choice(base_types._BaseFieldType):

	__slots__ = ["_AdddmInitn", "_AdddmRspn", "_Amdmnt", "_AuthstnInitn", "_AuthstnRspn", "_CardMgmtInitn", "_CardMgmtRspn", "_ChrgBckInitn", "_ChrgBckRspn", "_Err", "_FeeColltnInitn", "_FeeColltnRspn", "_FileActnInitn", "_FileActnRspn", "_FinInitn", "_FinRspn", "_FrdDspstnInitn", "_FrdDspstnRspn", "_FrdRptgInitn", "_FrdRptgRspn", "_KeyXchgInitn", "_KeyXchgRspn", "_NqryInitn", "_NqryRspn", "_NtwkMgmtInitn", "_NtwkMgmtRspn", "_RcncltnInitn", "_RcncltnRspn", "_RtrvlFlfmtInitn", "_RtrvlFlfmtRspn", "_RtrvlInitn", "_RtrvlRspn", "_RvslInitn", "_RvslRspn", "_SttlmRptgInitn", "_SttlmRptgRspn", "_VrfctnInitn", "_VrfctnRspn"]
	@property
	def AdddmInitn(self):
		return self._AdddmInitn

	@AdddmInitn.setter
	def AdddmInitn(self, value):
		self._AdddmInitn = value if value is not None else base_types.UninitialisedField(self, 'AdddmInitn', Max2MBBinary, False)

	@AdddmInitn.deleter
	def AdddmInitn(self):
		del self._AdddmInitn
		self._AdddmInitn = base_types.UninitialisedField(self, 'AdddmInitn', Max2MBBinary, False)

	@property
	def AdddmRspn(self):
		return self._AdddmRspn

	@AdddmRspn.setter
	def AdddmRspn(self, value):
		self._AdddmRspn = value if value is not None else base_types.UninitialisedField(self, 'AdddmRspn', Max2MBBinary, False)

	@AdddmRspn.deleter
	def AdddmRspn(self):
		del self._AdddmRspn
		self._AdddmRspn = base_types.UninitialisedField(self, 'AdddmRspn', Max2MBBinary, False)

	@property
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if value is not None else base_types.UninitialisedField(self, 'Amdmnt', Max2MBBinary, False)

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = base_types.UninitialisedField(self, 'Amdmnt', Max2MBBinary, False)

	@property
	def AuthstnInitn(self):
		return self._AuthstnInitn

	@AuthstnInitn.setter
	def AuthstnInitn(self, value):
		self._AuthstnInitn = value if value is not None else base_types.UninitialisedField(self, 'AuthstnInitn', Max2MBBinary, False)

	@AuthstnInitn.deleter
	def AuthstnInitn(self):
		del self._AuthstnInitn
		self._AuthstnInitn = base_types.UninitialisedField(self, 'AuthstnInitn', Max2MBBinary, False)

	@property
	def AuthstnRspn(self):
		return self._AuthstnRspn

	@AuthstnRspn.setter
	def AuthstnRspn(self, value):
		self._AuthstnRspn = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRspn', Max2MBBinary, False)

	@AuthstnRspn.deleter
	def AuthstnRspn(self):
		del self._AuthstnRspn
		self._AuthstnRspn = base_types.UninitialisedField(self, 'AuthstnRspn', Max2MBBinary, False)

	@property
	def CardMgmtInitn(self):
		return self._CardMgmtInitn

	@CardMgmtInitn.setter
	def CardMgmtInitn(self, value):
		self._CardMgmtInitn = value if value is not None else base_types.UninitialisedField(self, 'CardMgmtInitn', Max2MBBinary, False)

	@CardMgmtInitn.deleter
	def CardMgmtInitn(self):
		del self._CardMgmtInitn
		self._CardMgmtInitn = base_types.UninitialisedField(self, 'CardMgmtInitn', Max2MBBinary, False)

	@property
	def CardMgmtRspn(self):
		return self._CardMgmtRspn

	@CardMgmtRspn.setter
	def CardMgmtRspn(self, value):
		self._CardMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'CardMgmtRspn', Max2MBBinary, False)

	@CardMgmtRspn.deleter
	def CardMgmtRspn(self):
		del self._CardMgmtRspn
		self._CardMgmtRspn = base_types.UninitialisedField(self, 'CardMgmtRspn', Max2MBBinary, False)

	@property
	def ChrgBckInitn(self):
		return self._ChrgBckInitn

	@ChrgBckInitn.setter
	def ChrgBckInitn(self, value):
		self._ChrgBckInitn = value if value is not None else base_types.UninitialisedField(self, 'ChrgBckInitn', Max2MBBinary, False)

	@ChrgBckInitn.deleter
	def ChrgBckInitn(self):
		del self._ChrgBckInitn
		self._ChrgBckInitn = base_types.UninitialisedField(self, 'ChrgBckInitn', Max2MBBinary, False)

	@property
	def ChrgBckRspn(self):
		return self._ChrgBckRspn

	@ChrgBckRspn.setter
	def ChrgBckRspn(self, value):
		self._ChrgBckRspn = value if value is not None else base_types.UninitialisedField(self, 'ChrgBckRspn', Max2MBBinary, False)

	@ChrgBckRspn.deleter
	def ChrgBckRspn(self):
		del self._ChrgBckRspn
		self._ChrgBckRspn = base_types.UninitialisedField(self, 'ChrgBckRspn', Max2MBBinary, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', Max2MBBinary, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', Max2MBBinary, False)

	@property
	def FeeColltnInitn(self):
		return self._FeeColltnInitn

	@FeeColltnInitn.setter
	def FeeColltnInitn(self, value):
		self._FeeColltnInitn = value if value is not None else base_types.UninitialisedField(self, 'FeeColltnInitn', Max2MBBinary, False)

	@FeeColltnInitn.deleter
	def FeeColltnInitn(self):
		del self._FeeColltnInitn
		self._FeeColltnInitn = base_types.UninitialisedField(self, 'FeeColltnInitn', Max2MBBinary, False)

	@property
	def FeeColltnRspn(self):
		return self._FeeColltnRspn

	@FeeColltnRspn.setter
	def FeeColltnRspn(self, value):
		self._FeeColltnRspn = value if value is not None else base_types.UninitialisedField(self, 'FeeColltnRspn', Max2MBBinary, False)

	@FeeColltnRspn.deleter
	def FeeColltnRspn(self):
		del self._FeeColltnRspn
		self._FeeColltnRspn = base_types.UninitialisedField(self, 'FeeColltnRspn', Max2MBBinary, False)

	@property
	def FileActnInitn(self):
		return self._FileActnInitn

	@FileActnInitn.setter
	def FileActnInitn(self, value):
		self._FileActnInitn = value if value is not None else base_types.UninitialisedField(self, 'FileActnInitn', Max2MBBinary, False)

	@FileActnInitn.deleter
	def FileActnInitn(self):
		del self._FileActnInitn
		self._FileActnInitn = base_types.UninitialisedField(self, 'FileActnInitn', Max2MBBinary, False)

	@property
	def FileActnRspn(self):
		return self._FileActnRspn

	@FileActnRspn.setter
	def FileActnRspn(self, value):
		self._FileActnRspn = value if value is not None else base_types.UninitialisedField(self, 'FileActnRspn', Max2MBBinary, False)

	@FileActnRspn.deleter
	def FileActnRspn(self):
		del self._FileActnRspn
		self._FileActnRspn = base_types.UninitialisedField(self, 'FileActnRspn', Max2MBBinary, False)

	@property
	def FinInitn(self):
		return self._FinInitn

	@FinInitn.setter
	def FinInitn(self, value):
		self._FinInitn = value if value is not None else base_types.UninitialisedField(self, 'FinInitn', Max2MBBinary, False)

	@FinInitn.deleter
	def FinInitn(self):
		del self._FinInitn
		self._FinInitn = base_types.UninitialisedField(self, 'FinInitn', Max2MBBinary, False)

	@property
	def FinRspn(self):
		return self._FinRspn

	@FinRspn.setter
	def FinRspn(self, value):
		self._FinRspn = value if value is not None else base_types.UninitialisedField(self, 'FinRspn', Max2MBBinary, False)

	@FinRspn.deleter
	def FinRspn(self):
		del self._FinRspn
		self._FinRspn = base_types.UninitialisedField(self, 'FinRspn', Max2MBBinary, False)

	@property
	def FrdDspstnInitn(self):
		return self._FrdDspstnInitn

	@FrdDspstnInitn.setter
	def FrdDspstnInitn(self, value):
		self._FrdDspstnInitn = value if value is not None else base_types.UninitialisedField(self, 'FrdDspstnInitn', Max2MBBinary, False)

	@FrdDspstnInitn.deleter
	def FrdDspstnInitn(self):
		del self._FrdDspstnInitn
		self._FrdDspstnInitn = base_types.UninitialisedField(self, 'FrdDspstnInitn', Max2MBBinary, False)

	@property
	def FrdDspstnRspn(self):
		return self._FrdDspstnRspn

	@FrdDspstnRspn.setter
	def FrdDspstnRspn(self, value):
		self._FrdDspstnRspn = value if value is not None else base_types.UninitialisedField(self, 'FrdDspstnRspn', Max2MBBinary, False)

	@FrdDspstnRspn.deleter
	def FrdDspstnRspn(self):
		del self._FrdDspstnRspn
		self._FrdDspstnRspn = base_types.UninitialisedField(self, 'FrdDspstnRspn', Max2MBBinary, False)

	@property
	def FrdRptgInitn(self):
		return self._FrdRptgInitn

	@FrdRptgInitn.setter
	def FrdRptgInitn(self, value):
		self._FrdRptgInitn = value if value is not None else base_types.UninitialisedField(self, 'FrdRptgInitn', Max2MBBinary, False)

	@FrdRptgInitn.deleter
	def FrdRptgInitn(self):
		del self._FrdRptgInitn
		self._FrdRptgInitn = base_types.UninitialisedField(self, 'FrdRptgInitn', Max2MBBinary, False)

	@property
	def FrdRptgRspn(self):
		return self._FrdRptgRspn

	@FrdRptgRspn.setter
	def FrdRptgRspn(self, value):
		self._FrdRptgRspn = value if value is not None else base_types.UninitialisedField(self, 'FrdRptgRspn', Max2MBBinary, False)

	@FrdRptgRspn.deleter
	def FrdRptgRspn(self):
		del self._FrdRptgRspn
		self._FrdRptgRspn = base_types.UninitialisedField(self, 'FrdRptgRspn', Max2MBBinary, False)

	@property
	def KeyXchgInitn(self):
		return self._KeyXchgInitn

	@KeyXchgInitn.setter
	def KeyXchgInitn(self, value):
		self._KeyXchgInitn = value if value is not None else base_types.UninitialisedField(self, 'KeyXchgInitn', Max2MBBinary, False)

	@KeyXchgInitn.deleter
	def KeyXchgInitn(self):
		del self._KeyXchgInitn
		self._KeyXchgInitn = base_types.UninitialisedField(self, 'KeyXchgInitn', Max2MBBinary, False)

	@property
	def KeyXchgRspn(self):
		return self._KeyXchgRspn

	@KeyXchgRspn.setter
	def KeyXchgRspn(self, value):
		self._KeyXchgRspn = value if value is not None else base_types.UninitialisedField(self, 'KeyXchgRspn', Max2MBBinary, False)

	@KeyXchgRspn.deleter
	def KeyXchgRspn(self):
		del self._KeyXchgRspn
		self._KeyXchgRspn = base_types.UninitialisedField(self, 'KeyXchgRspn', Max2MBBinary, False)

	@property
	def NqryInitn(self):
		return self._NqryInitn

	@NqryInitn.setter
	def NqryInitn(self, value):
		self._NqryInitn = value if value is not None else base_types.UninitialisedField(self, 'NqryInitn', Max2MBBinary, False)

	@NqryInitn.deleter
	def NqryInitn(self):
		del self._NqryInitn
		self._NqryInitn = base_types.UninitialisedField(self, 'NqryInitn', Max2MBBinary, False)

	@property
	def NqryRspn(self):
		return self._NqryRspn

	@NqryRspn.setter
	def NqryRspn(self, value):
		self._NqryRspn = value if value is not None else base_types.UninitialisedField(self, 'NqryRspn', Max2MBBinary, False)

	@NqryRspn.deleter
	def NqryRspn(self):
		del self._NqryRspn
		self._NqryRspn = base_types.UninitialisedField(self, 'NqryRspn', Max2MBBinary, False)

	@property
	def NtwkMgmtInitn(self):
		return self._NtwkMgmtInitn

	@NtwkMgmtInitn.setter
	def NtwkMgmtInitn(self, value):
		self._NtwkMgmtInitn = value if value is not None else base_types.UninitialisedField(self, 'NtwkMgmtInitn', Max2MBBinary, False)

	@NtwkMgmtInitn.deleter
	def NtwkMgmtInitn(self):
		del self._NtwkMgmtInitn
		self._NtwkMgmtInitn = base_types.UninitialisedField(self, 'NtwkMgmtInitn', Max2MBBinary, False)

	@property
	def NtwkMgmtRspn(self):
		return self._NtwkMgmtRspn

	@NtwkMgmtRspn.setter
	def NtwkMgmtRspn(self, value):
		self._NtwkMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'NtwkMgmtRspn', Max2MBBinary, False)

	@NtwkMgmtRspn.deleter
	def NtwkMgmtRspn(self):
		del self._NtwkMgmtRspn
		self._NtwkMgmtRspn = base_types.UninitialisedField(self, 'NtwkMgmtRspn', Max2MBBinary, False)

	@property
	def RcncltnInitn(self):
		return self._RcncltnInitn

	@RcncltnInitn.setter
	def RcncltnInitn(self, value):
		self._RcncltnInitn = value if value is not None else base_types.UninitialisedField(self, 'RcncltnInitn', Max2MBBinary, False)

	@RcncltnInitn.deleter
	def RcncltnInitn(self):
		del self._RcncltnInitn
		self._RcncltnInitn = base_types.UninitialisedField(self, 'RcncltnInitn', Max2MBBinary, False)

	@property
	def RcncltnRspn(self):
		return self._RcncltnRspn

	@RcncltnRspn.setter
	def RcncltnRspn(self, value):
		self._RcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'RcncltnRspn', Max2MBBinary, False)

	@RcncltnRspn.deleter
	def RcncltnRspn(self):
		del self._RcncltnRspn
		self._RcncltnRspn = base_types.UninitialisedField(self, 'RcncltnRspn', Max2MBBinary, False)

	@property
	def RtrvlFlfmtInitn(self):
		return self._RtrvlFlfmtInitn

	@RtrvlFlfmtInitn.setter
	def RtrvlFlfmtInitn(self, value):
		self._RtrvlFlfmtInitn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlFlfmtInitn', Max2MBBinary, False)

	@RtrvlFlfmtInitn.deleter
	def RtrvlFlfmtInitn(self):
		del self._RtrvlFlfmtInitn
		self._RtrvlFlfmtInitn = base_types.UninitialisedField(self, 'RtrvlFlfmtInitn', Max2MBBinary, False)

	@property
	def RtrvlFlfmtRspn(self):
		return self._RtrvlFlfmtRspn

	@RtrvlFlfmtRspn.setter
	def RtrvlFlfmtRspn(self, value):
		self._RtrvlFlfmtRspn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlFlfmtRspn', Max2MBBinary, False)

	@RtrvlFlfmtRspn.deleter
	def RtrvlFlfmtRspn(self):
		del self._RtrvlFlfmtRspn
		self._RtrvlFlfmtRspn = base_types.UninitialisedField(self, 'RtrvlFlfmtRspn', Max2MBBinary, False)

	@property
	def RtrvlInitn(self):
		return self._RtrvlInitn

	@RtrvlInitn.setter
	def RtrvlInitn(self, value):
		self._RtrvlInitn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlInitn', Max2MBBinary, False)

	@RtrvlInitn.deleter
	def RtrvlInitn(self):
		del self._RtrvlInitn
		self._RtrvlInitn = base_types.UninitialisedField(self, 'RtrvlInitn', Max2MBBinary, False)

	@property
	def RtrvlRspn(self):
		return self._RtrvlRspn

	@RtrvlRspn.setter
	def RtrvlRspn(self, value):
		self._RtrvlRspn = value if value is not None else base_types.UninitialisedField(self, 'RtrvlRspn', Max2MBBinary, False)

	@RtrvlRspn.deleter
	def RtrvlRspn(self):
		del self._RtrvlRspn
		self._RtrvlRspn = base_types.UninitialisedField(self, 'RtrvlRspn', Max2MBBinary, False)

	@property
	def RvslInitn(self):
		return self._RvslInitn

	@RvslInitn.setter
	def RvslInitn(self, value):
		self._RvslInitn = value if value is not None else base_types.UninitialisedField(self, 'RvslInitn', Max2MBBinary, False)

	@RvslInitn.deleter
	def RvslInitn(self):
		del self._RvslInitn
		self._RvslInitn = base_types.UninitialisedField(self, 'RvslInitn', Max2MBBinary, False)

	@property
	def RvslRspn(self):
		return self._RvslRspn

	@RvslRspn.setter
	def RvslRspn(self, value):
		self._RvslRspn = value if value is not None else base_types.UninitialisedField(self, 'RvslRspn', Max2MBBinary, False)

	@RvslRspn.deleter
	def RvslRspn(self):
		del self._RvslRspn
		self._RvslRspn = base_types.UninitialisedField(self, 'RvslRspn', Max2MBBinary, False)

	@property
	def SttlmRptgInitn(self):
		return self._SttlmRptgInitn

	@SttlmRptgInitn.setter
	def SttlmRptgInitn(self, value):
		self._SttlmRptgInitn = value if value is not None else base_types.UninitialisedField(self, 'SttlmRptgInitn', Max2MBBinary, False)

	@SttlmRptgInitn.deleter
	def SttlmRptgInitn(self):
		del self._SttlmRptgInitn
		self._SttlmRptgInitn = base_types.UninitialisedField(self, 'SttlmRptgInitn', Max2MBBinary, False)

	@property
	def SttlmRptgRspn(self):
		return self._SttlmRptgRspn

	@SttlmRptgRspn.setter
	def SttlmRptgRspn(self, value):
		self._SttlmRptgRspn = value if value is not None else base_types.UninitialisedField(self, 'SttlmRptgRspn', Max2MBBinary, False)

	@SttlmRptgRspn.deleter
	def SttlmRptgRspn(self):
		del self._SttlmRptgRspn
		self._SttlmRptgRspn = base_types.UninitialisedField(self, 'SttlmRptgRspn', Max2MBBinary, False)

	@property
	def VrfctnInitn(self):
		return self._VrfctnInitn

	@VrfctnInitn.setter
	def VrfctnInitn(self, value):
		self._VrfctnInitn = value if value is not None else base_types.UninitialisedField(self, 'VrfctnInitn', Max2MBBinary, False)

	@VrfctnInitn.deleter
	def VrfctnInitn(self):
		del self._VrfctnInitn
		self._VrfctnInitn = base_types.UninitialisedField(self, 'VrfctnInitn', Max2MBBinary, False)

	@property
	def VrfctnRspn(self):
		return self._VrfctnRspn

	@VrfctnRspn.setter
	def VrfctnRspn(self, value):
		self._VrfctnRspn = value if value is not None else base_types.UninitialisedField(self, 'VrfctnRspn', Max2MBBinary, False)

	@VrfctnRspn.deleter
	def VrfctnRspn(self):
		del self._VrfctnRspn
		self._VrfctnRspn = base_types.UninitialisedField(self, 'VrfctnRspn', Max2MBBinary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdddmInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AdddmRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amdmnt', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AuthstnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AuthstnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CardMgmtInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CardMgmtRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChrgBckInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChrgBckRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FeeColltnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FeeColltnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FileActnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FileActnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FinInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FinRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdDspstnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdDspstnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdRptgInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdRptgRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyXchgInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyXchgRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NqryInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NqryRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtwkMgmtInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtwkMgmtRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcncltnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcncltnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmRptgInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmRptgRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VrfctnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VrfctnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
	))